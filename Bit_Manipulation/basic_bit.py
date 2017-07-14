    ''' if binary = 101101 and you want to find 2nd index of the binary.
    then * 1 << 2 = 100. Therefore when you & it.
      101101
    & 000100
    --------
      000100 which != 0 therefore it will return true.
      if get_bit is true then it is 1
      false then it is 0 '''

def get_bit (binary, ith):
    return ((binary & (1 << ith)) != 0)

    ''' if binary = 101101 and you want to have 1 in index 1.
    then 1 << 1 = 10
      101101
    | 000010
    --------
      101110 '''

def set_bit(binary, ith):
    return binary | (1 << ith)

    ''' if binary = 101101 then you want to clear the bit meaning instead 1 have 0.
    suppose you want to clear bit at index 2. then 1 << 2 = 100
    ~000100 = 111011
      101101
    & 111011
    ---------
      101001 '''

def clear_bit(binary, ith):
    return binary & ~(1 << ith)

    ''' if binary = 101101 and clear at 3
    (1 << 3) = 1000
    1000 - 1 = 111
      101101
    & 000111
    --------
      000101
    '''

def clear_bits_msb_through_i_inclusive(binary, ith):
    return binary & ((1 << ith) - 1)

    ''' if binary = 101101 and clear at 3
    (1 << (3 + 1)) = 10000
    10000 - 1 = 1111
    ~(001111) = 110000
      101101
    & 110000
    --------
      100000
     '''
def clear_bits_i_through_0_inclusive(binary,ith):
    return binary & ~((1 << (ith + 1)) - 1)

    ''' To set the ith bit to a value v, we first clear the bit at position i by using a mask that looks like 11101111.
Then, we shift the intended value, v, left by i bits. This will create a number with bit i equal to v and all
other bits equal to 0. Finally, we OR these two numbers, updating the ith bit if v is 1 and leaving it as 0
otherwise.

    '''

def update_bit(binary, ith, bit):
    return (binary & ~(1 << ith)) | (bit << ith)
