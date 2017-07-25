# Largest Continuous sum in an arry

def largeContSum(arr):
    if len(arr) == 0:
        return 0
    maxSum = arr[0]
    currentSum = arr[0]
    for number in arr[1:]:
        currentSum = max(currentSum+number, number)
        maxSum = max(currentSum, maxSum)
    return maxSum

print largeContSum([1, 2, -5])
