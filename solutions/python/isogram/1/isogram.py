def is_isogram(string):
    iso = []
    for let in string:
        if let != " " and let != "-" and let.lower() in iso:
            return False
        iso.append(let.lower())
    return True