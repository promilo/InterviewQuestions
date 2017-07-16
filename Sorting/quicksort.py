def quicksort(array):
    quicksortHelper(array, 0, len(array) - 1)

def quicksortHelper(array, leftIndex, rightIndex):
    #there are several ways to find pivot.
    # one option is to use the 1st element of the array as a pivot
    # or use the pivot from the middle.
    # the other way is to randomizee pivot.
    # i chose to do the median of the three of the first last and middle element.

    if leftIndex < rightIndex:
        print array
        border = partition(array, leftIndex, rightIndex)
        quicksortHelper(array, leftIndex, border - 1)
        quicksortHelper(array, border + 1, rightIndex)

def partition(arr, left, right):
    pIndex = find_pivot(arr, left, right)
    pVal = arr[pIndex]
    arr[pIndex], arr[left] = arr[left], arr[pIndex]
    border = left

    for i in range(left, right + 1):
        if arr[i] < pVal:
            border += 1
            arr[i], arr[border]  = arr[border], arr[i]
    arr[left], arr[border] = arr[border], arr[i]
    print "border, ", border
    return border

def find_pivot(array, leftIndex, rightIndex):
    middle = (leftIndex + rightIndex) // 2
    miniSort = sorted(array[leftIndex], array[middle], array[rightIndex])
    if miniSort[1] == array[leftIndex]:
        return leftIndex
    elif miniSort[1] == array[rightIndex]:
        return rightIndex
    return middle

quicksort([1,3,2])
