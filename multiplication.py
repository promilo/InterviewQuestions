def multiplication(n):
    maxmult = n * n
    maxlength = len(str(n*n)) + 1
    print maxlength
    print
    for i in range(1, n):
        for x in range(1, n):
            iterlength = len(str(i * x))
            numSpaces = maxlength - iterlength
            spaces = numSpaces * " "
            mult = i * x
            print spaces + str(mult),
        print

print multiplication(12)
