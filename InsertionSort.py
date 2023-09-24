def insertionSort(values):
    for i in range(1, len(values)):
        for j in range(i-1,-1,-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
            else:
                break
    return values



try:
    values = input("Enter the list of values seperated by spaces: ").split()
    values = [int(value) for value in values]
    print("Original List:", values)
    values = insertionSort(values)
    print("Sorted List:", values)

except ValueError as e:
    print(f"Error: {e}")
     