def square_of_sum(number):
    result = []
    for i in range(number):
        result.append(i+1)
    return sum(result)**2

def sum_of_squares(number):
    result = []
    for i in range(number):
        print(i)
        result.append((i+1)**2)
    return sum(result)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
