def quickSort(arr, threshold=10):
    quicksort2(arr, 0, len(arr)-1, threshold)
    return arr

def quicksort2(arr, low, hi, threshold):
    if hi - low < threshold and low < hi:
        quick_selection(arr, low, hi)
    elif low < hi:
        p = partition(arr, low, hi)
        quicksort2(arr, low, p-1, threshold)
        quicksort2(arr, p+1, hi, threshold)

def get_pivot(arr, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if arr[low] < arr[mid]:
        if arr[mid] < arr[hi]:
            pivot = mid
    elif arr[low] < arr[hi]:
        pivot = low
    return pivot

def partition(arr, low, hi):
    pivotIndex = get_pivot(arr, low, hi)
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]

    return border

def quick_selection(x, first, last):
    for i in range(first, last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]

try:
    arr = input("Enter the list of values separated by spaces: ").split()
    arr = [int(value) for value in arr]
    print("Original List:", arr)
    arr = quickSort(arr)
    print("Sorted List:", arr)

except ValueError as e:
    print(f"Error: {e}")

