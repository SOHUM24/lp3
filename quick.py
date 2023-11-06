def quicksort(alist, lower, higher):
    if lower < higher:
        p = partition(alist, lower, higher)
        quicksort(alist, lower, p - 1)
        quicksort(alist, p + 1, higher)


def partition(alist, lower, higher):
    pivot = alist[higher]
    i = lower
    j = lower

    while j < higher:
        if alist[j] <= pivot:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
        j += 1

    alist[i], alist[higher] = alist[higher], alist[i]

    return i


list_to_sort = [147, -16, 18, 91, 44, 1, 8, 54, 31, 18]
last_index = len(list_to_sort) - 1
quicksort(list_to_sort, 0, last_index)
print(list_to_sort)