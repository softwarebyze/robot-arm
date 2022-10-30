"""https://github.com/aakieu/3-dof-planar#readme
https://blog.robotiq.com/hs-fs/hubfs/Forward_Kinematics_Matrix.gif?width=591&name=Forward_Kinematics_Matrix.gif"""

from numpy import sin, cos, radians, dot, array

# Link lengths
a1, a2, a3, a4, a5, a6 = 1, 1, 1, 1, 1, 1

# Angles
theta_1 = radians(90)
theta_2 = radians(90)
theta_3 = radians(90)

# DH Parameter Table for 3 DOF Planar
#     [theta, alpha, r, d]
PT = [[theta_1, 0, a2, a1],
      [theta_2, 0, a4, a3],
      [theta_3, 0, a6, a5]]

# Homogeneous Transformation Matrices
H = []
for i in range(3):
    h = [[cos(PT[i][0]), -sin(PT[i][0]) * cos(PT[i][1]), sin(PT[i][0]) * sin(PT[i][1]), PT[i][2] * cos(PT[i][0])],
         [sin(PT[i][0]), cos(PT[i][0]) * cos(PT[i][1]), -cos(PT[i][0]) * sin(PT[i][1]), PT[i][2] * sin(PT[i][0])],
         [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]],
         [0, 0, 0, 1]]
    H.append(h)

H0_1, H1_2, H2_3 = H[0], H[1], H[2]

H0_1 = array(H0_1)
H0_2 = dot(H0_1, H1_2)
H0_3 = dot(H0_2, H2_3)

H0s = [H0_1, H0_2, H0_3]

transposed_matrices = [m.transpose() for m in H0s]
joint_coords = [m_t[-1][:2] for m_t in transposed_matrices]
print(joint_coords)
print('done')
# joint_coords.append()


# print("H0_1 =")
# print(matrix(array(H0_1).round(2)))
# print("H1_2 =")
# # print(matrix(H1_2))
# print(matrix(array(H1_2).round(2)))
# print("H2_3 =")
# # print(matrix(H2_3))
# print(matrix(array(H2_3).round(2)))


# print("H0_3 =")
# # print(matrix(H0_3))
# print(matrix(array(H0_3).round(2)))
