def check_brackets(string):
    tokens = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in string:
        if char in tokens:
            stack.append(tokens[char])
        elif char in tokens.values():
            if not stack or char != stack.pop():
                return False

    return not stack
