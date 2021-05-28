import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):

        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, numBalls):

        popBalls = []

        if numBalls >= len(self.contents):
            popBalls = self.contents
            self.contents = []
        else:
            for i in range(numBalls):
                index = random.randint(0, len(self.contents) - 1)
                popBalls.append(self.contents.pop(index))

        return popBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0

    ballsInHat = copy.deepcopy(hat.contents)

    for i in range(num_experiments):
        hat.contents = copy.deepcopy(ballsInHat)

        randomBalls = hat.draw(num_balls_drawn)

        m += probabalityMatch(randomBalls, expected_balls)

    return m / num_experiments


def probabalityMatch(actual, expected):
    seen = {}

    for i in actual:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    count = 0
    for i in expected:

        if i in seen:
            if seen[i] >= expected[i]:
                count += 1

    if count == len(expected):
        return 1
    return 0
