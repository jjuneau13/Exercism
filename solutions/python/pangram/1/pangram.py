def is_pangram(sentence):
    li = list(sentence)
    pang = set()
    for char in li:
        if char.isalpha():
            pang.add(char.lower())
    print(pang)
    return len(pang) == 26
