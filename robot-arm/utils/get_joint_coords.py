"""
Method for getting joint coordinates from link lengths
and joint angles
"""

from math import sin, cos, radians


def get_joint_coords(lengths: tuple | list,
                     angles: list[float],
                     origin: tuple = (0, 0),
                     precision: int | None = None
                     ) -> list[list[float]]:
    """
    Returns a list of joint coordinates given an origin, lengths, and angles

    # Example 1: 1 segment, horizontal
    >>> get_joint_coords(lengths=(1,), angles=[0])
    [[0, 0], [1, 0]]

    # Example 2: 2 segments, vertical
    >>> get_joint_coords([1,1],[90, 90])
    [[0, 0], [0, 1], [0, 2]]

    # Example 3: 1 segment with offset origin, horizontal to the left
    >>> get_joint_coords((1,),[180],(1,0))
    [[1, 0], [0, 0]]
    """
    if len(lengths) != len(angles):
        raise ValueError
    joints = [list(origin)]
    for i in range(1, len(lengths) + 1):
        joints.append([])
        joints[i] = [round(joints[i - 1][0] + lengths[i - 1] * cos(radians(angles[i - 1])), precision),
                     round(joints[i - 1][1] + lengths[i - 1] * sin(radians(angles[i - 1])), precision)]
    return joints
