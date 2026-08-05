def counting_sort(a,k):
    count = [0] * (k + 1)
    o = [0]*len(a)

    for i in range(len(a)):
        j = a[i]
        count[j] += 1
    for i in range(1, k + 1):
        count[i] = count[i] + count[i - 1]
    for i in range(len(a) - 1, -1, -1):
        j = a[i]
        count[j] = count[j] - 1
        o[count[j]] = a[i]
    return o


a = [234,31,3,54,73,34,2134,1,23,5,67,7,124,2,9999,4562,21]
k = len(a)

print(a)
print(counting_sort(a,max(a))) #qui il costo è O(n+k), se k = len(a) ---> O(n + n ) = O(n)
