def slices(series, length):
    if length <= 0 or len(series) < length:
        raise ValueError
    def compute_slice(series, length):
        return [list(map(int,series[i:i+length])) for i in range(0,len(series)-length+1)]
    return compute_slice(series, length)

