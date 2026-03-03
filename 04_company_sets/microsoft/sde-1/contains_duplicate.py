def containes_duplicate(s):
    s_set = set()

    for char in s:
        if char in s_set:
            return True
        s_set.add(char)