"""
Brute Force Inverse Kinematics Solver
This solver tries every possible combination of joint angles and
returns a RobotArm with angles closest to reaching the goal position.
The purpose is to have a simple but slow solver to use for comparing with
more advanced inverse kinematics solvers
TODO: bee colony algorithm?
"""

import itertools
from math import dist

from pandas import DataFrame

from robot_arm import RobotArm
from utils.get_joint_coords import get_joint_coords


def brute_force(robot: RobotArm, goal_pos: list | tuple) -> RobotArm:
    """Tries every possible angle combo and outputs the best RobotArm"""

    # first get an iterator of all possible angle permutations using the cartesian product
    possible_angles = list(itertools.product([i for i in robot.angle_range], repeat=len(robot.lengths)))

    # make a list of all the end effector coordinates for all the possible joint angles
    coords = []
    for angles in possible_angles:
        coords.append(get_joint_coords(robot.lengths, list(angles), origin=robot.origin, precision=3))

    # make a list with the distance from the goal to each combination of joint angles
    dists = []
    for coord in coords:
        dists.append(dist(goal_pos, coord[-1]))

    data = {'angle_combos': possible_angles,
            'coords': coords,
            'dists': dists}

    df = DataFrame(data).sort_values(by=['dists'])
    return RobotArm(robot.lengths, robot.origin, df['angle_combos'].iloc[0])


if __name__ == '__main__':
    test_robot = RobotArm([1, 1])
    gol = (0, 2)
    test_robot = brute_force(test_robot, gol)

    print(f'Joint Angles: \t{test_robot.joint_angles}')
