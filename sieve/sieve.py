def gen(limit):
    i = 2
    while i <= limit:
        yield i
        i += 1

def sieve(limit):
    prime_arr = list()
    for i in gen(limit):
        prime = True
        for a in range(2, i/2 + 1):
            if(i%a == 0):
                prime = False
                break
        if(prime):
            prime_arr.append(i)
    return prime_arr

