#!/usr/bin/python3
"""finds the peak of an unsorted list"""


def find_peak(list_of_integers):
    """finds the peak of a list"""

    if list_of_integers == []:
        return None

    li = list_of_integers
    length = len(li)
    mid = int(length/2)

    if mid-1 < 0 and mid+1 >= length:
        return li[mid]
    elif mid-1 < 0:
        if li[mid] > li[mid+1]:
            return li[mid]
        else:
            return li[mid+1]
    elif mid+1 >= length:
        if li[mid] > li[mid-1]:
            return li[mid]
        else:
            return li[mid-1]

    if li[mid] > li[mid+1] and li[mid] > li[mid-1]:
        return li[mid]
    else:
        pass

    if li[mid + 1] > li[mid - 1]:
        return find_peak(li[mid:])
    return find_peak(li[:mid])
