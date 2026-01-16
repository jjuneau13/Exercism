def response(hey_bob):
    stripped = hey_bob.strip()
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if stripped[-1] == "?":
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
