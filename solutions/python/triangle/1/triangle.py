def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and sides[0] != 0


def isosceles(sides):
    a, b, c = sides
    if a + b < c or a + c < b or b + c < a:
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sides
    if a + b < c or a + c < b or b + c < a:
        return False
    return a != b != c != a
