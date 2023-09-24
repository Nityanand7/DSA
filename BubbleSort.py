def bubbleSort(values):
    for i in range(0, len(values) - 1):
        for j in range(0, len(values)-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values
    
    
try:
    values = input("Enter the list of values seperated by spaces: ").split()
    values = [int(value) for value in values]
    print("Original List:", values)
    values = bubbleSort(values)
    print("Sorted List:", values)

except ValueError as e:
    print(f"Error: {e}")
