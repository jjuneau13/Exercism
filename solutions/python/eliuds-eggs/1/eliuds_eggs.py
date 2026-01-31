import math
def egg_count(display_value):
    count = 0
    bits = [2**x for x in range(13)]
    for bit in bits[::-1]:
        if bit <= display_value:
            display_value -= bit
            count += 1
    return count
    
