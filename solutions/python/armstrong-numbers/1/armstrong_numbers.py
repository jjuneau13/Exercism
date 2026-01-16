def is_armstrong_number(number):

    snum = str(number)
    sum = 0
    for digit in snum:
        sum += int(digit)**len(snum)
    return sum == number