import string 

def rows(letter):
    alpha = string.ascii_uppercase
    result = []
    count = (alpha.index(letter)+1)
    for i in range(count):
        temp = [" "] * (alpha.index(letter)+1)
        for y in range(len(temp)):
            if i == y:
                temp[i] = alpha[y]
        temp = temp[-1:0:-1] + temp
        result.append(''.join(temp))
    result.extend(result[-2::-1])
    return result
