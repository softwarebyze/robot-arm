import unittest

from brute_force import brute_force
from robot_arm import RobotArm


class TestBruteForce(unittest.TestCase):
    def test_brute_force(self):
        robot = RobotArm([1])
        goal_pos = (0, 1)
        self.assertEqual(brute_force(robot, goal_pos).joints[0], 90)


if __name__ == '__main__':
    unittest.main()
