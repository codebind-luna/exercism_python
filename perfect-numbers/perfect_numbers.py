def classify(number):
    factors = [1]
    total = 0

    if number < 1:
        raise ValueError
    elif number == 1:
        return "deficient"
    else:
        for i in range(2, int(number ** 0.5+1)):
            if number % i == 0:
                if (i != number / i):
                    factors.append(i)
                    factors.append(number / i)
                else:
                    factors.append(i)
    
    total = sum(factors)

    if total == number:
        return("perfect")
    elif total > number:
        return("abundant")
    else:
        return("deficient")
