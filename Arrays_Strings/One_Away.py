''' One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. '''
def one_away(str1, str2):
    if len(str1) == len(str2):
        diff = 0
        i = 0
        while i < len(str1):
            if str1[i] != str2[i]:
                if diff > 1:
                    return False
                else:
                    diff += 1
            i += 1
        return True
    else:
        if len(str1) > len(str2):
            index = 0
            i = 0
            while i < len(str2):
                if str2[i] != str1[i+index]:
                    if str2[i] != str1[i+1]:
                        return False
                    else:
                        if index != 1:
                            index+=1
                        else:
                            return False
                i += 1
            return True
        else:
            index = 0
            while i < len(str1):
                if str1[i] != str2[i+index]:
                    if str1[i] != str2[i+1]:
                        return False
                    else:
                        if index != 1:
                            index+=1
                        else:
                            return False
                i += 1
            return True

if __name__ == '__main__':
    print one_away("mil", "dil")
    print one_away("mil", "il")
    print one_away("mil", "sl")
