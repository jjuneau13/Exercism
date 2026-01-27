def abbreviate(words):
    words = words.replace('-', ' ').replace('_', '').split()
    print(words)
    result = ''
    for word in words:
        result += word[0].upper()
    return result
    
