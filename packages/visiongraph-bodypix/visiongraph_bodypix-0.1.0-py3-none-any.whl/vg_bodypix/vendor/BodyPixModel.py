import copy
from typing import Optional, List

import cv2
import numpy as np

from vg_bodypix.vendor.AbstractModel import AbstractModel
from vg_bodypix.vendor.types import Box


class BodyPix(AbstractModel):
    def __init__(
            self,
            *,
            runtime: Optional[str] = 'onnx',
            model_path: Optional[str] = 'bodypix_resnet50_stride16_1x3x480x640.onnx',
            providers: Optional[List] = None,
            strides: Optional[int] = None,
            map_score_th: float = 0.6
    ):
        """BodyPix

        Parameters
        ----------
        runtime: Optional[str]
            Runtime for BodyPix. Default: onnx

        model_path: Optional[str]
            ONNX/TFLite file path for BodyPix

        providers: Optional[List]
            Providers for ONNXRuntime.
        """
        super().__init__(
            runtime=runtime,
            model_path=model_path,
            providers=providers,
            map_score_th=map_score_th
        )
        self._swap = (2, 0, 1)
        self._mean = np.asarray([0.0, 0.0, 0.0])
        self._std = np.asarray([1.0, 1.0, 1.0])

        self.strides = strides

        # auto detect stride (needs onnx)
        if self.strides is None:
            import onnx
            model_proto = onnx.load(f=model_path)
            float_segments_raw_output = [v for v in model_proto.graph.value_info if
                                         v.name == 'float_segments_raw_output']
            if len(float_segments_raw_output) >= 1:
                w = float_segments_raw_output[0].type.tensor_type.shape.dim[-1].dim_value
                self.strides = self._input_shapes[0][self._w_index] // w

    def __call__(
            self,
            image: np.ndarray,
    ) -> List[Box]:
        """

        Parameters
        ----------
        image: np.ndarray
            Entire image

        Returns
        -------
        foreground_mask_zero_or_255: np.ndarray
            Predicted foreground mask: [batch, H, W, 3]. 0 or 255

        colored_mask_classid: np.ndarray
            Predicted colored mask: [batch, H, W, 1]. 0 - 24

        keypoints_classidscorexy: np.ndarray
            Predicted keypoints: [batch, N, 4]. classid, score, x, y
        """
        temp_image = copy.deepcopy(image)
        # PreProcess
        resized_image = \
            self._preprocess(
                temp_image,
            )
        # Inference
        inferece_image = np.asarray([resized_image], dtype=self._input_dtypes[0])
        outputs = super().__call__(input_datas=[inferece_image])
        foreground_mask_zero_or_255 = outputs[0]
        colored_mask_classid = outputs[1]
        keypoints_classidscorexy = outputs[2]
        # PostProcess
        result_foreground_mask_zero_or_255, result_colored_mask_classid, result_keypoints_classidscorexy = \
            self._postprocess(
                foreground_mask_zero_or_255=foreground_mask_zero_or_255,
                colored_mask_classid=colored_mask_classid,
                keypoints_classidscorexy=keypoints_classidscorexy,
            )
        return result_foreground_mask_zero_or_255, result_colored_mask_classid, result_keypoints_classidscorexy

    def _preprocess(
            self,
            image: np.ndarray,
    ) -> np.ndarray:
        """_preprocess

        Parameters
        ----------
        image: np.ndarray
            Entire image

        Returns
        -------
        resized_image: np.ndarray
            Resized and normalized image.
        """
        # Resize + Transpose
        resized_image = cv2.resize(
            image,
            (
                int(self._input_shapes[0][self._w_index]),
                int(self._input_shapes[0][self._h_index]),
            )
        )
        resized_image = resized_image[..., ::-1]
        resized_image = resized_image.transpose(self._swap)
        resized_image = \
            np.ascontiguousarray(
                resized_image,
                dtype=np.float32,
            )
        return resized_image

    def _postprocess(
            self,
            foreground_mask_zero_or_255: np.ndarray,
            colored_mask_classid: np.ndarray,
            keypoints_classidscorexy: np.ndarray,
    ) -> np.ndarray:
        """_postprocess

        Parameters
        ----------
        foreground_mask_zero_or_255: np.ndarray
            Predicted foreground mask: [batch, H, W, 3]. 0 or 255

        colored_mask_classid: np.ndarray
            Predicted colored mask: [batch, H, W, 1]. 0 - 24

        keypoints_classidscorexy: np.ndarray
            Predicted keypoints: [batch, N, 4]. classid, score, x, y

        Returns
        -------
        foreground_mask_zero_or_255: np.ndarray
            Predicted foreground mask: [batch, H, W, 3]. 0 or 255

        colored_mask_classid: np.ndarray
            Predicted colored mask: [batch, H, W, 1]. 0 - 24

        keypoints_classidscorexy: np.ndarray
            Predicted keypoints: [batch, N, 4]. classid, score, x, y
        """
        foreground_mask_zero_or_255 = foreground_mask_zero_or_255[0]  # 1 batch
        foreground_mask_zero_or_255 = foreground_mask_zero_or_255.transpose(1, 2, 0).astype(np.uint8)  # [H, W, 3]
        colored_mask_classid = colored_mask_classid[0]  # 1 batch
        colored_mask_classid = colored_mask_classid.transpose(1, 2, 0).astype(np.uint8)  # [H, W, 1]
        keypoints_classidscorexy = keypoints_classidscorexy[0]  # 1 batch
        return foreground_mask_zero_or_255, colored_mask_classid, keypoints_classidscorexy
