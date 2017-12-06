WINK = 1
DBLINK = int('10', 2)
CEYES = int('100', 2)
JUMP = int('1000', 2)
REV = int('10000', 2)


def handshake(number):
    steps = list()
    if isinstance(number, str):
        try:
            number = int(number, 2)
        except ValueError:
            return []
    if number < 0:
        return []
    if number & WINK:
        steps.append("wink")
    if number & DBLINK:
        steps.append("double blink")
    if number & CEYES:
        steps.append("close your eyes")
    if number & JUMP:
        steps.append("jump")
    if number & REV:
        steps = list(reversed(steps))
    return steps


def code(secret_code):
    num = 0
    for item in secret_code:
        if item not in ["wink", "double blink", "close your eyes", "jump"]:
            return '0'
    if "wink" in secret_code:
        num += WINK
    if "double blink" in secret_code:
        num += DBLINK
    if "close your eyes" in secret_code:
        num += CEYES
    if "jump" in secret_code:
        num += JUMP
    if handshake(num) != secret_code and handshake(num + REV) == secret_code:
        num += REV
    return "{:b}".format(num)
