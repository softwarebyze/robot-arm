import matplotlib.pyplot as plt
from numpy import array

coords = [array([3.18408168e-16, 5.20000000e+00]), array([-6.9, 5.2]), array([-6.9, -1.6])]

print(coords)

for coord in coords:
    # plt.scatter(coord[0], coord[1])
    plt.plot(coord)

plt.show()
