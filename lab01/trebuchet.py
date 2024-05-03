
from math import cos, sin, sqrt
from math import radians
import random
import matplotlib.pyplot as plt
import numpy as np

range = [50, 340]
v = 50
h = 100

target = random.randrange(range[0], range[1])
print("Target is at: ", target)

running = True

while(running):

    angle = radians(int(input("Enter the angle: ")))

    sqrt_val = (v * sin(angle))**2 + 2 * 10 * h
    
    if sqrt_val < 0:
        print("Invalid parameters, please try again.")
        continue

    d = v * cos(angle) * (v * sin(angle) + sqrt(sqrt_val)) / 10

    if target - 5 <= d <= target + 5:
        print("Hit target!")
        running = False
        t_flight = v * np.sin(angle) + np.sqrt((v * np.sin(angle))**2 + 2 * 10 * h) / 10

        t = np.linspace(0, t_flight, num=10)
        x = v * np.cos(angle) * t
        y = h + v * np.sin(angle) * t - 0.5 * 10 * t**2
        plt.figure()
        plt.plot(x, y)
        plt.title('Trajektoria pocisku')
        plt.xlabel('Odległość (m)')
        plt.ylabel('Wysokość (m)')
        plt.grid(True)
        plt.show()
    else:
        if d < target - 5:
            print("Undershot")
        else:
            print("Overshot")

