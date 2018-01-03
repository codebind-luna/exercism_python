def board(input_board_array):
    # Function body starts here
    around = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    if len(set(map(len, input_board_array))) > 1:
        raise ValueError('rows are not of equal length')
    for i in range(0,len(input_board_array)):
        input_board_array[i] = input_board_array[i].replace(' ','0')
    for i in range(0,len(input_board_array)):
        for j in range(0,len(input_board_array[i])):
            if input_board_array[i][j] == '*':
                for k in range(0,len(around)):
                    if (i + around[k][0]) >= 0 and (i + around[k][0]) < len(input_board_array) and (j + around[k][1] >= 0) and (j + around[k][1]) < len(input_board_array[0]):
                        try:
                            input_board_array[i + around[k][0]] = input_board_array[i +
                            around[k][0]][:j + around[k][1]] + str(int(input_board_array[i +
                            around[k][0]][j + around[k][1]]) + 1) + input_board_array[i +
                            around[k][0]][j + around[k][1] + 1:]
                        except:
                            pass
            elif not input_board_array[i][j].isdigit():
                raise ValueError('invalid char encountered')
    for i in range(0,len(input_board_array)):
        input_board_array[i] = input_board_array[i].replace('0',' ')
    return input_board_array
