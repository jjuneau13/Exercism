def factors(value):
    number = value
    factors = []
    factor = 2
    while factor <= number:
        while number % factor == 0:
            number //= factor
            factors.append(factor)
        factor += 1
    return factors
