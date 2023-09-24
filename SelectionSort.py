def SelectionSort(values):
    for i in range(0, len(values) - 1):
        minIndex = i
        for j in range(i+1, len(values)):
            if values[j] < values[minIndex]:
                minIndex = j
        if minIndex!=i:
            values[i], values[minIndex] = values[minIndex], values[i]
    return values
    
    
try:
    values = input("Enter the list of values seperated by spaces: ").split()
    values = [int(value) for value in values]
    print("Original List:", values)
    values = SelectionSort(values)
    print("Sorted List:", values)

except ValueError as e:
    print(f"Error: {e}")