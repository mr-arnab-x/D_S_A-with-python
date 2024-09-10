def binary_search(list ,target):
    first = 0       ## define 0th index                 [1,2,3,4,5,6,7,8,9,10]
    last = len(list) - 1        ## define last index    [0,1,2,3,4,5,6,7,8,9] first index 0, last index = 9

    while first <= last:
        midpoint = (first + last) // 2          ## for integer value as a midpoint

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1 
        else:
            last = midpoint - 1         ## list[midpoint] > target

    return None

def verify(index):      ## index for midpoint
    if index is not None :
        print ("Target found at index : ",index)

    else :
        print("Target not found in the list")

number = [1,2,3,4,5,6,7,8,9,10]

# result = binary_search(number,12)

# verify(result)

result = binary_search(number,6)

verify(result)












"""

Key Differences:

    Binary Search (Iterative): " Uses loops, easier to understand and manage because it just repeats the process until it finds the item. "

    Recursive Binary Search: " Uses recursion (a function calling itself), which can be harder to grasp at first but is often seen as more elegant for certain problems. "

"""














