def sum_of_multiples(limit, multiples):
    multilist = set([])
    for mult in multiples:
        for i in range(1, (limit/mult + 1)):
            if mult * i < limit:
                multilist.add(mult*i)
    return sum(multilist)
