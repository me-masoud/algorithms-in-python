import math


def binary_search(haystack, needle, end, begin=0):
    mid = int((end + begin) / 2)
    if needle == haystack[mid]:
        return mid
    if begin == end and needle == haystack[begin]:
        return begin

    if needle < haystack[mid]:
        return binary_search(haystack, needle,  mid - 1, begin)
    else:
        return binary_search(haystack, needle, end, mid + 1)


print(binary_search([1, 50, 400, 555, 666, 700, 1000], 1000, 6))
