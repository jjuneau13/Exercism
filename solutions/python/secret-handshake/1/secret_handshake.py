def commands(binary_str):
    shake = []
    rev = binary_str[::-1]
    print(rev)
    for num in range(len(binary_str)):
        print(num, rev[num], shake)
        if rev[num] == '1':
            if num == 0:
                shake.append('wink')
            if num == 1:
                shake.append('double blink')
            if num == 2:
                shake.append('close your eyes')
            if num == 3:
                shake.append('jump')
            if num == 4:
                shake = shake[::-1]
    return shake
