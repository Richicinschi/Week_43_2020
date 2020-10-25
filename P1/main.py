import random
import math


def circleAreaMC(n):
    pointsInCirle = 0
    totalPoints = n
    for i in range (0, totalPoints):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if math.sqrt(x**2 + y**2) < 0.5:
            pointsInCirle = pointsInCirle + 1
    area = 4 * (float(pointsInCirle/totalPoints))
    return area

if __name__ == '__main__':
    f = int(input("give a number of points wanted :"))
    print("result is :",circleAreaMC(f))
