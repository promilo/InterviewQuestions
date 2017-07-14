''' Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and j. Write a method
to insert Minto N such that M starts at bit j and ends at bit i. You can assume that the bits j through
i have enough space to fit all of M. That is, if M = 18811, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
fit between bit 3 and bit 2.
EXAMPLE
Input: N Ul811 , i 2, j 6
Output: N = 18881881188 '''

''' the way to solve this is to clear the bits from i to j. you can do this with and opeartor with 0s.
but at the same time you have to keep the values from i to to the right  and j to the left.
so essentaillyou you want something like this & 11000111.  then in the end or with m.
to get something like 11000111 you can do a complement of 111000. The trick is to subtract 1000000 - 1 to get 111000.
'''

def updateBits(n, m, i, j):
    cleared_n = n & ~((1 << (j + 1)) - (1 << i))
    print "1 << (j + 1)", bin((1 << (j + 1))) # shift 1 to 100000
    print "1 << (j + 1) - (1 << i)", bin(((1 << (j + 1)) - (1 << i))) # 100000 - 1000 = 111000
    print bin(cleared_n) #000111
    shifted_m = m << i
    print bin(shifted_m) # shifted 0b101 to 101000
    return cleared_n | shifted_m



print bin(updateBits(0b1011010, 0b101, 3, 5))
