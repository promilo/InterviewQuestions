def geteven(arr):
    counts = {}
    for num in arr:
        if num in counts.keys():
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count % 2 == 0:
            return num

print geteven([1,2,2,3,4,4,5,5,6,6,6,6,2,3,2,3,1,1,1,1])
