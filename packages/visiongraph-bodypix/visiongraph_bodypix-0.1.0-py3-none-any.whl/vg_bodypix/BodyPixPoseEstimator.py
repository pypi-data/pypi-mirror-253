from enum import Enum
from typing import Optional, List, Tuple

import cv2
import numpy as np
from visiongraph.data.Asset import Asset
from visiongraph.data.RepositoryAsset import RepositoryAsset
from visiongraph.estimator.spatial.pose.PoseEstimator import PoseEstimator
from visiongraph.model.geometry.Size2D import Size2D
from visiongraph.result.ResultList import ResultList
from visiongraph.util import ImageUtils
from visiongraph.util.VectorUtils import list_of_vector4D

from vg_bodypix.BodyPixPose import BodyPixPose
from vg_bodypix.vendor.BodyPixModel import BodyPix
from vg_bodypix.vendor.utils import affine_transform, extract_max_score_points_unique


class BodyPixPoseConfig(Enum):
    RESNET_S16_256x320 = RepositoryAsset("bodypix_resnet50_stride16_1x3x256x320.onnx"), 16
    RESNET_S16_384x288 = RepositoryAsset("bodypix_resnet50_stride16_Nx3x384x288.onnx"), 16
    RESNET_S16_480x640 = RepositoryAsset("bodypix_resnet50_stride16_1x3x480x640.onnx"), 16
    RESNET_S16_640x640 = RepositoryAsset("bodypix_resnet50_stride16_1x3x640x640.onnx"), 16
    RESNET_S16_736x1280 = RepositoryAsset("bodypix_resnet50_stride16_1x3x736x1280.onnx"), 16


class BodyPixPoseEstimator(PoseEstimator[BodyPixPose]):
    def __init__(self, model_asset: Asset, strides: Optional[int] = None,
                 min_score: float = 0.2, mask_min_score: float = 0.6):
        super().__init__(min_score)

        self.mask_min_score: float = mask_min_score

        self.model_asset = model_asset

        self.model: Optional[BodyPix] = None
        self.strides: Optional[int] = strides

        self.runtime: str = "openvino"
        self.providers: List[str] = ["AUTO"]

        self.padding_color = (114, 114, 114)

    def setup(self):
        self.model = BodyPix(
            model_path=self.model_asset.path,
            providers=self.providers,
            runtime=self.runtime,
            strides=self.strides,
            map_score_th=self.mask_min_score
        )

    def process(self, image: np.ndarray) -> ResultList[BodyPixPose]:
        h, w = image.shape[:2]
        tensor_w, tensor_h = self.model.input_size

        # pad input
        padded_image, pad_box = ImageUtils.resize_and_pad(image, (tensor_w, tensor_h), color=self.padding_color)

        # inference
        foreground_mask_zero_or_255, colored_mask_classid, keypoints_classidscorexy = self.model(padded_image)

        # post-process masks
        ft_foreground_mask, ft_mask_class_id = self._fine_tune_mask_position(foreground_mask_zero_or_255,
                                                                             colored_mask_classid,
                                                                             tensor_w, tensor_h)

        # remove padding of output masks
        ft_foreground_mask = ImageUtils.roi(ft_foreground_mask, pad_box)
        ft_mask_class_id = ImageUtils.roi(ft_mask_class_id, pad_box)

        # resize if necessary to match original size
        if ft_foreground_mask.shape[0] != h or ft_foreground_mask.shape[1] != w:
            ft_foreground_mask = cv2.resize(ft_foreground_mask, (w, h))

        if ft_mask_class_id.shape[0] != h or ft_mask_class_id.shape[1] != w:
            ft_mask_class_id = cv2.resize(ft_mask_class_id, (w, h))

        # eliminate low score keypoints
        score_keep = keypoints_classidscorexy[..., 1] >= self.min_score
        keypoints_classidscorexy = keypoints_classidscorexy[score_keep, :]

        # extract single keypoints (max scores)
        if len(keypoints_classidscorexy) > 0:
            keypoints_classidscorexy = extract_max_score_points_unique(keypoints_classidscorexy, 5)

            # only get unique values
            unique_first_values, unique_indices = np.unique(keypoints_classidscorexy[:, 0], return_index=True)
            keypoints_classidscorexy = keypoints_classidscorexy[unique_indices]
            unique_keypoints = list(keypoints_classidscorexy)

            # add empty keypoints to always have 17
            if len(unique_keypoints) != 17:
                all_points = set(keypoints_classidscorexy[:, 0].astype(int))
                for i in range(17):
                    if i in all_points:
                        continue
                    unique_keypoints.insert(i, np.array([i, -1, 0, 0], dtype=float))
        else:
            unique_keypoints = []

        # create visiongraph output
        results = ResultList()
        for raw_pose in [unique_keypoints]:
            key_points: List[Tuple[float, float, float, float]] = []

            score_sum = 0
            for index, score, x, y in raw_pose:
                key_points.append((x / tensor_w, y / tensor_h, 0.0, score))
                score_sum += score

            score_sum /= len(raw_pose)

            pose = BodyPixPose(float(score_sum), list_of_vector4D(key_points),
                               cv2.cvtColor(ft_foreground_mask, cv2.COLOR_BGR2GRAY),
                               ft_mask_class_id.squeeze())
            results.append(pose)

        # fix padding of key-points
        pose.map_coordinates(Size2D(tensor_w, tensor_h), Size2D.from_image(image), src_roi=pad_box)
        return results

    def _fine_tune_mask_position(self,
                                 foreground_mask_zero_or_255: np.ndarray,
                                 colored_mask_classid: np.ndarray,
                                 input_width: int, input_height: int) -> Tuple[np.ndarray, np.ndarray]:

        # Fine-tune position of mask image
        number_of_fine_tuning_pixels: int = self.model.strides // 2
        if number_of_fine_tuning_pixels > 0:
            foreground_mask_zero_or_255 = \
                affine_transform(
                    image=foreground_mask_zero_or_255,
                    height=input_height,
                    width=input_width,
                    dx=-number_of_fine_tuning_pixels,
                    dy=-number_of_fine_tuning_pixels,
                )
            colored_mask_classid = \
                affine_transform(
                    image=colored_mask_classid,
                    height=input_height,
                    width=input_width,
                    dx=-number_of_fine_tuning_pixels,
                    dy=-number_of_fine_tuning_pixels,
                )[..., np.newaxis]
        return foreground_mask_zero_or_255, colored_mask_classid

    def release(self):
        pass

    @staticmethod
    def create(config: BodyPixPoseConfig = BodyPixPoseConfig.RESNET_S16_480x640) -> "BodyPixPoseEstimator":
        asset, strides = config.value
        return BodyPixPoseEstimator(asset, strides=strides)
