def liner_search(list,target):
    for i in range(0,len(list)):    ## i for index
        if list[i] == target :
            return i
        
def verify(index):      ## index for i
    if index is not None :
        print ("Target found at index : ",index)

    else :
        print("Target not found in the list")

number = [1,2,3,4,5,6,7,8,9,10]

# result = liner_search(number,12)

result = liner_search(number,6)

verify(result)
