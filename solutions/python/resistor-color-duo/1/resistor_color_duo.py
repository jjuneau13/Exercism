def value(colors):
    colors_li = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return int(str(colors_li.index(colors[0]))+  str(colors_li.index(colors[1])))
