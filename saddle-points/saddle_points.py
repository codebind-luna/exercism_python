def saddle_points(matrix):
    saddles = list()
    row_maxes = [max(x) for x in matrix]
    col_mins  = [min(x) for x in zip(*matrix)]
    for idx_r, row in enumerate(matrix):
        if len(row) != len(matrix[0]):
            raise ValueError
        for idx_c, item in enumerate(row):
            if item == row_maxes[idx_r] and item == col_mins[idx_c]:
                saddles.append((idx_r, idx_c))
    return set(saddles)
