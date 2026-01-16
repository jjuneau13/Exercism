def square(number):
    if number == 1:
        return 1
    elif 1 < number <= 64:
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")


def total():
    grains = 0
    for box in range(64):
        grains += square(box+1)
    return grains
