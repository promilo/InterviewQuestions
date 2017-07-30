def isShuffle(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if not s1 or not s2 or not s3:
        if s1 + s2 == s3:
            return True
        else:
            return False

    if s1[0] != s3[0] and s2[0] != s3[0]:
        return False

    if s1[0] == s3[0] and isShuffle(s1[1:], s2, s3[1:]):
        return True
    if s2[0] == s3[0] and isShuffle(s1, s2[1:], s3[1:]):
        return True

    return False
