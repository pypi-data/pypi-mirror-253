import cv2
import numpy as np


def extract_max_score_points_unique(points: np.ndarray, radius: int = 20):
    """
    Extracts the points with the maximum score within a specified radius for each classid, ensuring uniqueness.

    Parameters:
    points (np.ndarray): An array of shape [n, 4] where each row represents [classid, score, x, y].
    radius (float): The radius within which to search for points.

    Returns:
    np.ndarray: An array of extracted unique points with the maximum score within the specified radius for each classid.
    """
    # Initialize an empty list to store the maximum score points
    max_score_points = []
    # Iterate over each unique classid in the array
    for classid in np.unique(points[:, 0]):
        class_points = points[points[:, 0] == classid]
        while class_points.size > 0:
            # Take the first point as the reference
            reference_point = class_points[0]
            _, _, ref_x, ref_y = reference_point
            # Calculate the distance from the reference point to all other points in the same class
            distances = np.sqrt((class_points[:, 2] - ref_x) ** 2 + (class_points[:, 3] - ref_y) ** 2)
            # Filter points within the specified radius
            within_radius = class_points[distances <= radius]
            # Find the point with the maximum score within the radius
            if within_radius.size > 0:
                max_score_point = within_radius[within_radius[:, 1].argmax()]
                max_score_points.append(max_score_point)
            # Remove the selected points from the class_points
            class_points = np.array([point for point in class_points if list(point) not in within_radius.tolist()])
    # Convert the list of points back to a NumPy array
    return np.array(max_score_points)


def affine_transform(image: np.ndarray, width: int, height: int, dx: int, dy: int) -> np.ndarray:
    # Create a transformation matrix for a parallel shift
    affine_matrix = np.float32([[1, 0, dx], [0, 1, dy]])

    # apply an infinite transformation
    affine_image = \
        cv2.warpAffine(
            src=image,
            M=affine_matrix,
            dsize=(width, height)
        )
    return affine_image
