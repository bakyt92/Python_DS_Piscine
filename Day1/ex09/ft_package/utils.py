def count_in_list(lst, word):
    i = 0
    for x in lst:
        if x == word:
            i += 1
    return i