def tripletsum(arr):
    for i in enumerate(arr):
        for o in range(i[0] + 1, len(arr)):
            print o, arr[o]

tripletsum([1,2,3])
