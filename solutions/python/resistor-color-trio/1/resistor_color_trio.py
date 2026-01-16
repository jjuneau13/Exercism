def label(colors):
    colorli = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    first = colorli.index(colors[0])
    second = colorli.index(colors[1])
    third = colorli.index(colors[2])
    trailZ = ""
    if second == 0:
        third += 1
    if third == 9:
        trailZ = " giga"
    elif third >= 6:
        third -= 6
        trailZ = "0"*third + " mega"
    elif third >= 3:
        third -= 3
        trailZ = "0"*third + " kilo"
    else:
        trailZ = "0"*third + " "

    if first == 0 and second == 0:
        return f"{trailZ}ohms"
    if first == 0:
        return f"{second}{trailZ}ohms"
    if second == 0:
        return f"{first}{trailZ}ohms"
    return f"{first}{second}{trailZ}ohms"