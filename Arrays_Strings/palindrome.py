'''Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words. '''

def is_palindrome(str):
    med = len(str)/2
    count = 0
    for i in str[:med]:
        if i != str[len(str)-1-count]:
            return False
        else:
            count +=1
    return True




if __name__ == '__main__':
    print is_palindrome("anana")
    print is_palindrome("Milind")
