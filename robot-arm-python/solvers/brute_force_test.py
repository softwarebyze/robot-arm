import unittest

from brute_force import brute_force
from robot_arm import RobotArm


class TestBruteForce(unittest.TestCase):

    def test_brute_force(self):
        """test for vertical position"""
        robot = RobotArm([1])
        goal_pos = (0, 1)
        self.assertEqual(brute_force(robot, goal_pos).joint_angles[0], 90)

    def test1_brute_force(self):
        """test for horizontal position"""
        robot = RobotArm([1])
        goal_pos = (1, 0)
        self.assertEqual(brute_force(robot, goal_pos).joint_angles[0], 0)

    def test2_brute_force(self):
        """test for vertical position with two joint_angles"""
        robot = RobotArm([1, 1])
        goal_pos = (0, 2)
        self.assertEqual(brute_force(robot, goal_pos).joint_angles, [90, 90])


if __name__ == '__main__':
    unittest.main()
