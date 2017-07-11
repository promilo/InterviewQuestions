# Return true if a string has all unique characters.

def is_unique(str):
    array = []
    for i in str:
        if i not in array:
            array.append(i)
        else:
            return False
    return True

# time complexity O(n)
# Space Complexity O(n)

# If we cannot use data structures
def no_struct_is_unique(str):
    count = 0
    for i in str:
        count += 1
        for n in str[count:]:
            if i == n:
                return False
    return True

# Time Complexity O(n^2)
# Space Complexity O(1)

if __name__ == '__main__':
    print is_unique("milo")
    print is_unique("milind")
    print no_struct_is_unique("milo")
    print no_struct_is_unique("milind")
