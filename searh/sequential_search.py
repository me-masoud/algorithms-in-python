## this is sequential search or linier search

def seqSearch(n, haystack, needle):
    i = 0
    while i < n:
        if needle == haystack[i]:
            return i
        ++i

    return -1
