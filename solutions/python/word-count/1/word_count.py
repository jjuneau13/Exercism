import string
def count_words(sentence):
    words = {}
    alpha = string.ascii_lowercase + "'1234567890"
    current = ""
    for letter in range(len(sentence)):
        if sentence[letter].lower() in alpha:
            current += sentence[letter].lower()
            continue
        current = current.strip("'")
        if current in words:
            words[current] += 1
        elif current != "":
            words[current] = 1
        current = ""
    current = current.strip("'")
    if current in words:
        words[current] += 1
    elif current != "":
        words[current] = 1
    return words
        
    