def MergeSort(arr):
    MergeSort2(arr, 0, len(arr)-1 )
    return arr

def MergeSort2(arr, first, last):
    if first<last:
        middle = (first + last)//2
        MergeSort2(arr, first, middle)
        MergeSort2(arr, middle+1, last)
        merge(arr, first, middle, last)

def merge(A, first, middle, last):
    L = arr[first:middle+1]
    R = arr[middle+1:last+1]
    L.append(999999999)
    R.append(999999999)
    i=j=0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1

try:
    arr = input("Enter the list of values seperated by spaces: ").split()
    arr = [int(value) for value in arr]
    print("Original List:", arr)
    arr = MergeSort(arr)
    print("Sorted List:", arr)

except ValueError as e:
    print(f"Error: {e}")