def fence_pattern(rails, message_size):
    matrix = [[None for i in range(message_size)] for j in range(rails)]
    row = 0
    d = -1
    for i in range(message_size):
        matrix[row][i] = '*'
        if row == 0 or row == rails - 1:
            d *= -1
        row += d
    return matrix

def encode(message, rails):
    matrix = fence_pattern(rails, len(message))

    row = 0
    d = -1
    for i in range(len(matrix[row])):
        matrix[row][i] = message[i]
        if row == 0 or row == rails - 1:
            d *= -1
        row += d

    result = ''
    for row in matrix:
        for col in row:
            if col is not None:
                result += col
    return result

def decode(encoded_message, rails):
    matrix = fence_pattern(rails, len(encoded_message))

    i = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '*':
                matrix[row][col] = encoded_message[i]
                i += 1

    result = ''
    row = 0
    d = -1
    for i in range(len(matrix[row])):
        result += matrix[row][i]
        if row == 0 or row == rails - 1:
            d *= -1
        row += d

    return result
