def recursive_binary_search(list,target):       ## gives true or false as output

    if len(list) == 0 :      ## check for empty list
        return False
    else :
        midpoint = (len(list)) // 2 

        if list[midpoint] == target :
            return True
        else :
            if list[midpoint] < target :
                return recursive_binary_search(list[midpoint + 1 : ] , target)      ## after (:)  blank part defines the end of the list in python
            
            else :
                return recursive_binary_search(list[ : midpoint],target)
            

def verify(result):
    print(" Target found : ",result)

number = [1,2,3,4,5,6,7,8,9,10]

# result = recursive_binary_search(number,12)
# verify(result)

result = recursive_binary_search(number,6)
verify(result)










"""

Key Differences:

    Binary Search (Iterative): " Uses loops, easier to understand and manage because it just repeats the process until it finds the item. "

    Recursive Binary Search: " Uses recursion (a function calling itself), which can be harder to grasp at first but is often seen as more elegant for certain problems. "

"""




