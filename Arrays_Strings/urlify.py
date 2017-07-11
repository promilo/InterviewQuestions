'''  Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string '''

def urlify (str):
    output = ""
    for i in str:
        if i == ' ':
            output += "%20"
        else:
            output += i
    return output





if __name__ == '__main__':
    print urlify("Milind is the Best")
