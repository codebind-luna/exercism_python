import random
from string import ascii_uppercase

class Robot(object):
    SEENNAMES = []

    def __init__(self):
        print(Robot.SEENNAMES)
        self.name = generate_name()

    def reset(self):
        self.name = generate_name()


def generate_name():
    lets = random.sample(ascii_uppercase, 2)
    nums = random.randrange(100, 1000)
    name = ''.join(lets) + str(nums)
    if name not in Robot.SEENNAMES:
        Robot.SEENNAMES.append(name)
        return name
    return generate_name()
