def largest_product(series, size):
    big = 0
    for i in range(0, len(series) - size + 1):
        temp_big = reduce(lambda x,y : int(x) * int(y), list(series[i:i+size]))
        if temp_big > big:
            big = temp_big
    return big
