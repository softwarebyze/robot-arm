"""
Robot Arm Class
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


class RobotArm:
    """
    Example:
                                       (O)  goal position = known or none
        lengths[1] = known             /
                                      /       joints[n] = known or calculated or none (angle of the joint)
                                     O   --- angle reference
        lengths[0] = known           |
                                     |        joints[0] = known or calculated or none (angle of the joint)
    origin = known or assumed        O   --- angle reference
    """

    def __init__(self,
                 lengths: list | tuple,
                 origin: tuple | None = (0, 0),
                 joints=None
                 ) -> None:
        self.lengths = lengths
        self.origin = origin
        self.joints = joints

    angle_range = range(0, 181)


if __name__ == "__main__":
    pass
