def transform(legacy_data):
    result = {}
    for score, value in legacy_data.items():
        for letter in value:
            result[letter.lower()] = score
    return result