import re

class Luhn(object):
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        number = self.number.replace(' ','')
        if not number.isdigit() or len(number) < 2:
            return False
        number = [int(n) for n in reversed(number)]
        return not sum(number[::2] + [ 2 * n if n < 5 else 2 * n - 9 for n in number[1::2]]) % 10
