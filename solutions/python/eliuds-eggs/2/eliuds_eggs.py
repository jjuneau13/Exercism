import math
def egg_count(display_value):
    count = 0
    while display_value > 0:
        print(display_value, display_value % 2)
        if display_value % 2 == 1:
            count += 1
        display_value //= 2
    return count
    
