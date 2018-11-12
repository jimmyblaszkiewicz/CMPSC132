

def quickSort(numList, start=0, end=None):
    if end is None:
        end = len(numList)-1

    if len(numList) <= 1:
        return numList

    if start < end:
        split = partition(numList, start, end)
        quickSort(numList, start, split-1)
        quickSort(numList, split +1, end)
        return numList


def partition(numList, first, last):
    # Last element as pivot
    pivot = numList[last]
    left = first 
    right = last-1

    done = False
    while not done:
        while numList[left] <= pivot and left <= right:
            left += 1

        while numList[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
            # right and left have crossed so we're done
        else: 
            # swap right and left
            numList[right], numList[left] = numList[left], numList[right]

    numList[last], numList[left] = numList[left], numList[last]

    return left
