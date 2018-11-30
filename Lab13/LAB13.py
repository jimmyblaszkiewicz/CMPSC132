#LAB 13
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name: Jimmy Blaszkiewicz
# Collaboration Statement: I worked on this program by myself using only the class materials             
#
########################################

def merge(list1, list2):
	#write your code here
    # merged list and two counters, one for left and right
    merged = []
    count1 = 0
    count2 = 0
    # keep count1 and count2 less than the length of their respective lists
    while count1 < len(list1) and count2 < len(list2):
        if list1[count1] < list2[count2]:
            merged.append(list1[count1])
            count1 += 1
        else:
            merged.append(list2[count2])
            count2 += 1

    # just append on what was left if one list was shorter than the other
    merged += list1[count1:]
    merged += list2[count2:]

    return merged



def mergeSort(numList):
	#write your code here
    # base case also takes into account if the list is size 0
    if len(numList) <= 1:
        return numList

    # cut list in half, call merge sort on each half, return the sorted lists merged together
    split = len(numList)//2
    left = mergeSort(numList[:split])
    right = mergeSort(numList[split:])
    
    return merge(left, right)
