''' Binary to String: Given a real number between 8 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print "ERROR:' '''

def printBinary(num):
    if num >= 1 or num <= 0:
        return "Error"
    half = 0.5
    output = "."
    while num > 0:
        print "num, ", num
        if len(output) > 32: # if the length is greater than 32 return error
            print "went greater than 32"
            return output
        if num >= half:
            output += "1"
            num -= half
        else:
            output += "0"
        half = half/2.0
    return output


print printBinary(0.32)
