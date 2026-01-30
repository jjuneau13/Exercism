def decode(string):
    result = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count:
                result += (char * int(count))
            else:
                result += char
            count = ""
    return result
    
def encode(string):
    current = ""
    count = 0
    result = ""
    for char in range(len(string)):
        if string[char] == current:
            count += 1
            if char + 1 == len(string):
                result += str(count) + string[char]
        else:
            if count > 1:
                result += str(count)
            result += current
            if char + 1 == len(string):
                result += string[char]
            current = string[char]
            count = 1
    return result
