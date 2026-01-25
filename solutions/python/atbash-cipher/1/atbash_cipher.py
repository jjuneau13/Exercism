import string

def encode(plain_text):
    alpha = string.ascii_lowercase
    plain_text = ''.join(char for char in plain_text if char not in string.punctuation)
    plain_text = plain_text.replace(' ', '').lower()
    print(plain_text)
    rev = alpha[::-1]
    result = []
    for i in range(len(plain_text)):
        if i % 5 == 0 and i > 0:
            result.append(" ")
        if plain_text[i] in alpha:
            result.append(rev[alpha.index(plain_text[i])])
        if plain_text[i].isnumeric():
            result.append(plain_text[i])
    return ''.join(result)

def decode(plain_text):
    alpha = string.ascii_lowercase
    plain_text = ''.join(char for char in plain_text if char not in string.punctuation)
    plain_text = plain_text.replace(' ', '').lower()
    print(plain_text)
    rev = alpha[::-1]
    result = []
    for i in range(len(plain_text)):
        if plain_text[i] in alpha:
            result.append(rev[alpha.index(plain_text[i])])
        if plain_text[i].isnumeric():
            result.append(plain_text[i])
    return ''.join(result)
