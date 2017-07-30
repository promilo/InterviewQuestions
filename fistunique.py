def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    letters='abcdefghijklmnopqrstuvwxyz'
    print s.count("a")
    index=[s.index(l) for l in letters if s.count(l) == 1]
    print index
    return s[min(index)] if len(index) > 0 else -1

print firstUniqChar("abacadabra")
