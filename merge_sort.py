def merge_sort(list):
    """
    Sorts a list in ascending order
    returns the new sorted list
    
    Divide: find the most midpoint of the list and divide into sublists 
    conquer: recursively sort the sublists created in the previous step 
    combine: Merge the sorted sublists created in the previous step
    takes O(n log n) time
    """ 

    if len(list) <= 1:
        return list 
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """ 
    Divide unsorted list at the midpoint into sublists
    Returns two sublists left and right
    takes O(log n) time
    """

    midpoint = len(list) // 2

    countI = 0
    left = []
    while countI < midpoint:
        left.append(list[countI])
        countI += 1

    countJ = len(list) -1 
    right = []
    while countJ > midpoint:
        right.append(list[countJ])
        countJ -= 1

    # listValues = list(list.values())
    # right = listValues.slice(left)

    return left, right

def merge(left, right):
    """
    merges two lists (array) together, sorting them in the process.
    Returns a new merged list
    runs in overall O(n) time 
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist = [52, 26, 262 , 29, 73]
l = merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))
