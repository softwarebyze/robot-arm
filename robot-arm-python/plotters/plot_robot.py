"""
Plot a Robot
"""
import matplotlib.pyplot as plt

from ..robot_arm import RobotArm
from ..utils.get_joint_coords import get_robot_coords


def show_robot(robot: RobotArm, axes=None, show: bool = True) -> None:
    if robot.coords is None:
        robot.coords = get_robot_coords(robot)
    x, y = [coord[0] for coord in robot.coords], [coord[1] for coord in robot.coords]
    if axes:
        axes.plot(x, y)
    else:
        plt.plot(x, y)
    if show:
        plt.show()


def show_robots(robots: [RobotArm]) -> None:
    for robot in robots:
        if robot.coords is None:
            robot.coords = get_robot_coords(robot)
        x, y = [coord[0] for coord in robot.coords], [coord[1] for coord in robot.coords]

        plt.plot(x, y)
    plt.show()


#
# def get_robot_fig(robot: RobotArm) -> plt.Figure:
#     """Returns a figure of the robot"""
#     fig = plt.figure()
#     # plot origin
#     plt.scatter(x=robot.origin[0], y=robot.origin[1], label="Origin")
#
#     # plot goal position
#     # plt.scatter(x=goal_pos[0], y=goal_pos[1], label="Goal")
#
#     # plot first possibility
#     # plt.scatter(x=coords[0][0], y=coords[0][1], label="First possibility")
#     # plt.plot(x=[coord[0] for coord in coords[0]], y=[coord[1] for coord in coords[0]], label="First possibility")
#     # plot_pop(sorted_possible_angles, lengths=LENGTHS, start_pos=robot.origin)
#     # plot the best possibility
#     # plt.scatter(x=sorted_coords[0][0], y=sorted_coords[0][1], label="Best")
#     # plt.scatter(x=sorted_coords[0][-1][0], y=sorted_coords[0][-1][1], label="Best")
#
#     # plt.plot(sorted_dists, label="sorted_dists")
#
#     plt.legend()
#     plt.show()
#     return plt
#
#
# if __name__ == '__main__':
#     robot_fig = get_robot_fig(RobotArm([1], joint_angles=[45]))
#     robot_fig.show()
print('done')
