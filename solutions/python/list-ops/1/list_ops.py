def append(list1, list2):
    list1 += list2
    return list1


def concat(lists):
    result = []
    for i in lists:
        result += i
    return result


def filter(function, list):
    result = []
    for i in list:
        if function(i):
            result += [i]
    return result


def length(list):
    result = 0
    for i in list:
        result += 1
    return result


def map(function, list):
    result = []
    for i in list:
        result += [function(i)]
    return result


def foldl(function, list, initial):
    for i in list:
        initial = function(initial, i)
    return initial


def foldr(function, list, initial):
    for i in list[::-1]:
        initial = function(initial, i)
    return initial


def reverse(list):
    return list[::-1]
