def line_up(name, number):
    if (number-1)%10 == 0 and number != 11:
        number = str(number) + 'st'
    elif (number-2)%10 == 0 and number%100 != 12:
        number = str(number) + 'nd'
    elif (number-3)%10 == 0 and number != 13:
        number = str(number) + 'rd'
    else:
        number = str(number) + 'th'
    return f'{name}, you are the {number} customer we serve today. Thank you!'
