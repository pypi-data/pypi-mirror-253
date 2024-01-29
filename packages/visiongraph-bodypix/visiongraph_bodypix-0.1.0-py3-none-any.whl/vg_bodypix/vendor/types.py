from dataclasses import dataclass

BODY_COLORS = [
    (110, 64, 170), (143, 61, 178), (178, 60, 178), (210, 62, 167),
    (238, 67, 149), (255, 78, 125), (255, 94, 99), (255, 115, 75),
    (255, 140, 56), (239, 167, 47), (217, 194, 49), (194, 219, 64),
    (175, 240, 91), (135, 245, 87), (96, 247, 96), (64, 243, 115),
    (40, 234, 141), (28, 219, 169), (26, 199, 194), (33, 176, 213),
    (47, 150, 224), (65, 125, 224), (84, 101, 214), (99, 81, 195)
]

PART_NAMES = [
    'nose', 'leftEye', 'rightEye', 'leftEar', 'rightEar', 'leftShoulder',
    'rightShoulder', 'leftElbow', 'rightElbow', 'leftWrist', 'rightWrist',
    'leftHip', 'rightHip', 'leftKnee', 'rightKnee', 'leftAnkle', 'rightAnkle'
]

PART_CHANNELS = [
    'left_face',
    'right_face',
    'left_upper_arm_front',
    'left_upper_arm_back',
    'right_upper_arm_front',
    'right_upper_arm_back',
    'left_lower_arm_front',
    'left_lower_arm_back',
    'right_lower_arm_front',
    'right_lower_arm_back',
    'left_hand',
    'right_hand',
    'torso_front',
    'torso_back',
    'left_upper_leg_front',
    'left_upper_leg_back',
    'right_upper_leg_front',
    'right_upper_leg_back',
    'left_lower_leg_front',
    'left_lower_leg_back',
    'right_lower_leg_front',
    'right_lower_leg_back',
    'left_feet',
    'right_feet'
]


@dataclass(frozen=False)
class Box:
    classid: int
    score: float
    x1: int
    y1: int
    x2: int
    y2: int
