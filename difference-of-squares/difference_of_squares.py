def square_of_sum(upto):
    sum = 0
    for i in range(1, upto  + 1):
        sum += i
    return sum ** 2


def sum_of_squares(upto):
    sum = 0
    for i in range(1, upto + 1):
        sum += (i ** 2)
    return sum 


def difference(upto):
    return square_of_sum(upto) - sum_of_squares(upto)
