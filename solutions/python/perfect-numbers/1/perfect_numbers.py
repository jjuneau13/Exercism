def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = []
    for int in range(number-1):
        if number%(int+1) == 0:
            factors.append(int+1)
    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"
    else:
        return "deficient"
