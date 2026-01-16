def resistor_label(colors):
    color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    tolerance_list = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}
    num = f"{color.index(colors[0])}"
    if len(colors) > 1:
        trail = color.index(colors[-2]) * "0"
        result = f"±{tolerance_list[colors[-1]]}%"
        if len(colors) == 4:
            num = num + f"{color.index(colors[1])}{trail}"
        if len(colors) == 5:
            num = num + f"{color.index(colors[1])}{color.index(colors[2])}{trail}"
        if len(num) > 6:
            num = int(num)
            num = num/1000000
            result = f"{num:g} megaohms {result}"
        elif len(num) >3:
            num = int(num)
            num = num/1000
            result = f"{num:g} kiloohms {result}"
        else:
            result = f"{num} ohms {result}"
    else:
        result = f"{num} ohms"
    return result