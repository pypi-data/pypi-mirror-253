from typing import Optional, Sequence

import numpy as np
import vector
from visiongraph.result.spatial.InstanceSegmentationResult import InstanceSegmentationResult
from visiongraph.result.spatial.pose.COCOPose import COCOPose
from visiongraph.result.spatial.pose.PoseLandmarkResult import POSE_DETECTION_ID, POSE_DETECTION_NAME

from vg_bodypix.vendor.types import BODY_COLORS


class BodyPixPose(COCOPose, InstanceSegmentationResult):
    def __init__(self, score: float, landmarks: vector.VectorNumpy4D, mask: np.ndarray, body_parts_map: np.ndarray):
        COCOPose.__init__(self, score, landmarks)
        InstanceSegmentationResult.__init__(self, POSE_DETECTION_ID, POSE_DETECTION_NAME,
                                            score, mask, self.bounding_box)
        self.body_parts_map = body_parts_map

    def annotate(self, image: np.ndarray, show_info: bool = True, info_text: Optional[str] = None,
                 color: Optional[Sequence[int]] = None,
                 show_bounding_box: bool = False, min_score: float = 0, use_class_color: bool = True, **kwargs):
        if self.mask is not None:
            InstanceSegmentationResult.annotate(self, image, show_info, info_text, show_bounding_box,
                                                use_class_color, min_score, **kwargs)
        COCOPose.annotate(self, image, show_info, info_text, color, show_bounding_box, min_score, **kwargs)

    @property
    def colored_part_map(self):
        _part_colors = BODY_COLORS
        part_colors_array = np.asarray(_part_colors)
        default_color = (0, 0, 0)

        # np.take will take the last value if the index is -1
        part_colors_with_default_array = np.append(
            part_colors_array,
            np.asarray([default_color]),
            axis=-2
        )

        part_segmentation_colored = np.take(
            part_colors_with_default_array,
            self.body_parts_map,
            axis=-2
        )

        return part_segmentation_colored.astype(np.uint8)
