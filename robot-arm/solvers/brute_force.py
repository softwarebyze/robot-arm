"""
Brute Force Inverse Kinematics Solver
This solver tries every possible combination of joint angles and
returns a RobotArm with angles closest to reaching the goal position.
The purpose is to have a simple but slow solver to use for comparing with
more advanced inverse kinematics solvers
"""

import itertools
from math import dist

from robot_arm import RobotArm
from utils.get_joint_coords import get_joint_coords


def brute_force(robot: RobotArm, goal_pos) -> RobotArm:
    """tries every possible angle combo and outputs the best RobotArm"""
    # first get a list of all possible angle permutations using the cartesian product
    possible_angles = []
    for combo in itertools.product(robot.angle_range, repeat=len(robot.lengths)):
        possible_angles.append(combo)  # this gives a list of tuples

    # make a list of all the end effector coordinates for all the possible joint angles
    coords = []
    for angles in possible_angles:
        coords.append(get_joint_coords(robot.lengths, list(angles), origin=robot.origin))

    # make a list with the distance from the goal of each combination of joint angles
    dists = []
    for coord in coords:
        dists.append(dist(goal_pos, coord[-1]))

    # sort list of possible joint angles by distance to goal position by dist
    # sorted_dists = sorted(dists)
    sorted_possible_angles = [a for d, a in sorted(zip(dists, possible_angles))]
    # sorted_coords = [c for d, c in sorted(zip(dists, coords))]

    return RobotArm(robot.lengths, robot.origin, sorted_possible_angles[0])


test_robot = RobotArm([1])

# test_robot = brute_force(test_robot, (0, 1))
print(brute_force(test_robot, (0, 1)).joints[-1])
# print(test_robot.joints)
# print(get_joint_coords(test_robot.lengths, list(test_robot.joints)))
# print('done')
