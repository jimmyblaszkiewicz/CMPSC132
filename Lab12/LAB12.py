#LAB 12
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program by myself 
#                          using only the class materials             
#
########################################


def bubbleSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
        2nd returned value: the sorted list

        >>> bubbleSort([2,3,5,4,1])
        ({1: [2, 3, 4, 1, 5], 2: [2, 3, 1, 4, 5], 3: [2, 1, 3, 4, 5], 4: [1, 2, 3, 4, 5]}, [1, 2, 3, 4, 5])
    '''
    # Your code starts here

    passes = {}
    counter = 1
    swaps = True

    # do one pass outside the loop
    while swaps:
        swaps = False
        # until there are no swaps in one pass, keep passing through

        for i in range(len(numList)-1):
            if numList[i] > numList[i+1]:
                swaps = True
                numList[i], numList[i+1] = numList[i+1], numList[i]
        
        if swaps:
            # need to use a copy bc lists are mutable
            passes[counter] = numList.copy()
            counter += 1

    return (passes, numList)
