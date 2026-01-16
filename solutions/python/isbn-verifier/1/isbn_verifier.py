def is_valid(isbn):
    lisbn = list(isbn)
    mult = 10
    result = 0
    for char in lisbn:
        if char == "-":
            continue
        if char == 'X':
            result += 10 
            mult -= 1
        elif char.isnumeric():
            result += int(char) * mult
            mult -= 1 
        else:
            return False
        print(result)
    return result % 11 == 0 and mult == 0
