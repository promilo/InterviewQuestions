def firstNotRepeatingCharacter(s):

    count = {}
    for index, char in enumerate(s):
        if char in count.keys():
            count[char]["count"] += 1
        else:
            count[char] = {"index": index, "count": 1}

    minIndex = len(s)
    for char in count.keys():
        if count[char]["index"] < minIndex and count[char]["count"] == 1:
            minIndex = count[char]["index"]

    if minIndex == len(s):
        return "_"
    return s[minIndex]
