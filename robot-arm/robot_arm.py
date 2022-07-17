"""
Robot Arm Class
"""


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
