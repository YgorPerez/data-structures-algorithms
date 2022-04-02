def binary_search(list, target):
    listLength = len(list)
    first = 0
    last = listLength - 1
    count = 1
    while (first <= last):
        midpoint = (first + last)//2 
        if list[midpoint] == target:
            print("It took", count, "iterations to complete")
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
        count += 1
    return None

def verify(index): 
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in listLength")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 6)
verify(result)
