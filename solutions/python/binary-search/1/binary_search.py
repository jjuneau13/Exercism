def find(search_list, value):
    try:
        return search_list.index(value)
    except:
        raise ValueError("value not in array")
    """if search_list[len(search_list)//2] == value:
        return 
    if search_list[len(search_list)//2] < value:
        return find(search_list[len(search_list)//2:])
    else:
        return """