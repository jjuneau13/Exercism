def find_anagrams(word, candidates):
    sorted_word = sorted(list(word.lower()))
    anagram = []
    for item in candidates:
        if item.lower() == word.lower():
            continue
        sor = sorted(list(item.lower()))
        print(sor)
        if sor == sorted_word:
            anagram.append(item)
    print(anagram)
    return anagram