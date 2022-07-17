"""
Brute Force Inverse Kinematics Solver
This solver tries every possible combination of joint angles and
returns a RobotArm with angles closest to reaching the goal position.
The purpose is to have a simple but slow solver to use for comparing with
more advanced inverse kinematics solvers
"""

import itertools
from math import dist

from utils.get_joint_coords import get_joint_coords

"""
Goal: try all positions and return closest ones to goal position.
Assumption: Joint has a range of 0 to 180 deg as in SG90 servos
Given an origin, lengths, and goal position,
for every combination of angles for len(lengths) joints,
compute the resulting end effector position.
Compute the distance to the goal position.
Sort the combos by increasing distance.
Return the first 5 in a list.
# If any combos have distance 0, add them as the solution list.
# Else if any combos have distance rounded to integer == 0, add them to solution list (but keep the unrounded distance).
# Else 

Example:
                     O  goal position = [2*cos(90)+2*cos(45), 2*sin(90)+2*sin(45)] ~= [1.414, 3.414]
lengths[1] = 2      /   
                   /       45 deg
                  O   --- angle reference
lengths[0] = 2    | 
                  |        90 deg
origin = (0,0)    O   --- angle reference

solutions[example] = [90,45]

"""


def brute_force(robot: RobotArm, goal_pos) -> RobotArm:
    """tries every possible angle combo and outputs the best RobotArm"""
    # first get a list of all possible angle permutations. how: cross product
    possible_angles = []
    for combo in itertools.product(robot.angle_range, repeat=2):
        possible_angles.append(combo)  # this gives a list of tuples

    coords = []
    for angles in possible_angles:
        # coords.append(get_joint_coords(LENGTHS, list(angles), origin=ORIGIN, precision=PRECISION)[-1])
        coords.append(get_joint_coords(robot.lengths, list(angles), origin=robot.origin))

    dists = []
    for coord in coords:
        dists.append(dist(goal_pos, coord[-1]))

    # sort everything by dist
    sorted_dists = sorted(dists)
    sorted_possible_angles = [a for d, a in sorted(zip(dists, possible_angles))]
    sorted_coords = [c for d, c in sorted(zip(dists, coords))]

    return RobotArm(robot.lengths, robot.origin, sorted_possible_angles[0])


if __name__ == "__main__":
    LENGTHS = (1, 1)
    # START_POS = (0, 0)
    PRECISION = 5
    # GOAL_POS = (round(1.41, PRECISION), round(3.41, PRECISION))
    GOAL_POS = (0, 2)
    ORIGIN = (0, 0)
    angle_range = range(0, 180 + 1)
    BotArm = RobotArm(lengths=LENGTHS, origin=ORIGIN)
    best = brute_force(BotArm, GOAL_POS)
    print(best.joints)
