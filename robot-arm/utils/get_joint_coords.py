"""
Method for getting joint coordinates from link lengths
and joint angles
"""

from math import sin, cos, radians


def get_joint_coords(lengths: tuple | list,
                     angles: list[float],
                     origin: tuple = (0, 0),
                     precision: int | None = 2
                     ) -> list[list[float]]:
    """
    Returns a list of joint coordinates given an origin, lengths, and angles

    # Example 1: 1 segment, horizontal
    >>> get_joint_coords(lengths=(1,), angles=[0], precision=None) #without mapping
    [[0, 0], [1, 0]]

    # >>> get_joint_coords(lengths=(1,), angles=[90], precision=None) #with mapping
    # [[0, 0], [1, 0]]
    #
    # # Example 1a: 1 segment, horizontal
    # >>> get_joint_coords(lengths=(1,), angles=[90], precision=None)
    >>> get_joint_coords(lengths=(1,), angles=[90], precision=None)
    [[0, 0], [0, 1]]

    # Example 2: 2 segments, vertical
    >>> get_joint_coords(lengths=[1, 1],angles=[90, 0], precision=None)
    [[0, 0], [0, 1], [0, 2]]

    # Example 3: 1 segment with offset origin, horizontal to the left
    >>> get_joint_coords((1,),[180],origin=(1,0), precision=None)
    [[1, 0], [0, 0]]

    # Example 4: 2 segments
    >>> get_joint_coords(lengths=(1, 1, 1), angles=[90, -90, -90], precision=None)
    [[0, 0], [0, 1], [1, 1], [1, 0]]
    """
    assert len(lengths) == len(angles), "Expecting same number of lengths and angles"
    input_angles = angles
    # angles = [interp(a, [0, 180], [-90, 90]) for a in angles]
    # angles = [interp(a, [-90, 90], [0, 180]) for a in angles]

    joint_coords = [list(origin)]  # joint_coords = [[0, 0]]
    for i in range(1, len(lengths) + 1):  # for i in 1, 2, ... , n (number of links) = (1, 2)
        joint_coords.append([])  # joint_coords = [[0, 0], []]
        joint_coords[i] = [  # joint_coords[1] = [[0, 0], [
            round(joint_coords[i - 1][0] + (lengths[i - 1] * cos(radians(sum(angles[:i])))), precision),
            round(joint_coords[i - 1][1] + (lengths[i - 1] * sin(radians(sum(angles[:i])))), precision)]
    return joint_coords


if __name__ == "__main__":
    test_lengths = [1, 1]
    test_angles = [90, 90]
    my_coords = get_joint_coords(test_lengths, test_angles, precision=None)
    print(f'A planar robot has {len(test_lengths)} links and {len(test_angles)} joints that rotate.')
    print(f'The lengths are: {test_lengths}')
    print(f'The joint angles are: {test_angles}')
    print(input('What do you expect the joint coords to be?\n'))
    print(my_coords)
