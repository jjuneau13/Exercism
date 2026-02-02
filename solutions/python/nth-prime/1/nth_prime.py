import math
def prime(number):
    if number <= 0:
        raise ValueError("there is no zeroth prime")
    primes = [2, 3]
    prime = 4
    while len(primes) < number:
        for i in range(2, math.isqrt(prime)+1):
            if prime % i == 0:
                break
            if i == math.isqrt(prime):
                primes.append(prime)
        prime += 1
    return primes[number-1]