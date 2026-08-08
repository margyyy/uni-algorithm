def minimum(a):
    min = a[0]
    for i in range (1,len(a)):
        if min > a[i]:
            min = a[i]
    return min

a = [12,3,4,235,5,3,2,165]
print(minimum(a))
