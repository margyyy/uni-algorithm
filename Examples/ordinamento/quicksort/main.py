def partition(a, p, r):
    pivot = a[p]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q)
        quicksort(a, q + 1, r)


a = [12, 53, 1, 24, 5, 3, 124, 6, 1, 7, 45, 23]

print("Prima:", a)

quicksort(a, 0, len(a) - 1)

print("Dopo: ", a)
