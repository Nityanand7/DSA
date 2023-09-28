def linearSearch(arr,x):
    for i in range(0,len(arr)):
        if(arr[i]==x):
            return i
    return -1


try:
    arr = input("Enter the list of values separated by spaces: ").split()
    arr = [int(value) for value in arr]
    x = int(input("Enter the element you want to search "))
    result = linearSearch(arr,x)
    if(result==-1):
        print("Element not found")
    else:
        print("Element found at index: ",result)
        

except ValueError as e:
    print(f"Error: {e}")