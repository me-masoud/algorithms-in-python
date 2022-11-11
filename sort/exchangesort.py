def exchange_sort(n, haystack):
    i = 1
    while i < n:
        j = 1
        while j <= i:
            if haystack[i - j + 1] < haystack[i - j]:
                tmp = haystack[i - j]
                haystack[i - j] = haystack[i - j + 1]
                haystack[i - j + 1] = tmp
            j += 1

        i += 1
    return haystack


print(exchange_sort(5, [2, 45, 21, 3, 2]))
