import string

def rotate(text, key):
    alphabetUP = string.ascii_uppercase * 2
    alphabetLOW = string.ascii_lowercase * 2
    result = ""
    for let in text:
        if let in alphabetLOW:
            result += alphabetLOW[alphabetLOW.index(let) + key]
        elif let in alphabetUP:
            result += alphabetUP[alphabetUP.index(let) + key]
        else:
            result += let
        print(result)
    return result
