def score(x, y):
    rad = 0
    if x == 0:
        rad = abs(y)
    elif y == 0:
        rad = abs(x)
    else:
        rad = (abs(x)**2 + abs(y)**2)**(1/2)

    if rad <= 1:
        return 10
    elif rad <= 5:
        return 5
    elif rad <= 10:
        return 1
    else:
        return 0