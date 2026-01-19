def sum_of_multiples(limit, multiples):
    result = []
    for multiple in multiples:
        if multiple != 0:
            for i in range(1, limit):
                if i % multiple == 0:
                    result.append(i)
    return sum(set(result))
