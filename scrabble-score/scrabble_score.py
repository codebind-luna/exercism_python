dict     = {}
dict[1]  = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
dict[2]  = ['D', 'G']
dict[3]  = ['B', 'C', 'M', 'P']
dict[4]  = ['F', 'H', 'V', 'W', 'Y']
dict[5]  = ['K']
dict[8]  = ['J', 'X']
dict[10] = ['Q', 'Z']

def score(word):
    return sum([get_score(dict, x.upper()) for x in list(word)])

def get_score(dict, char):
    for key, value in dict.items():
        if char in value:
            return int(key)
