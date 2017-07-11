# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        return True
    else:
        return False

#More efficient solution. One way to do this is to keep track of character counts

def efficient_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        s1 = {}
        s2 = {}
        for i in str1:
            if i not in s1:
                s1[i] = 1
            else:
                s1[i] += 1
        for x in str2:
            if x not in s2:
                s2[x] = 1
            else:
                s2[x] += 1
        return s1 == s2


if __name__ == '__main__':
    print is_permutation("god", "dog")
    print is_permutation("cool", "coos")
    print efficient_permutation("god", "dog")
    print efficient_permutation("cool", "coos")
