def is_armstrong(number):
    n = str(number)
    power = len(n)
    return number == sum([int(d)**power for d in n])
