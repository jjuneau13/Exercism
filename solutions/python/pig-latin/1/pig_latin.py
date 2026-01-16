def translate(text):
    vowels = 'aeiou'
    result = []
    for word in text.split(' '):
        if (word[0] in vowels) or (word[:2] in ['xr', 'yt']):
            result.append(word + 'ay')
            continue
        for i in range(len(word)):
            if word[i] in vowels or (word[i] == 'y' and i != 0):
                result.append(word[i:] + word[:i] + 'ay')
                break
            elif word[i:i+2] == 'qu':
                result.append(word[i+2:] + word[:i+2] +'ay')
                break
            elif word[i] == 'y' and i == 0:
                result.append(word[i+1:] + word[:i+1] +'ay')
                break
    return ' '.join(result)