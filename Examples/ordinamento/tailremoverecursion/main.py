def somma_notail(n, t):
    if n > t:
        return 0

    return n + somma_notail(n + 1, t)


def somma_tail(n, t, accumulatore=0):
    if n > t:
        return accumulatore

    return somma_tail(n + 1, t, accumulatore + n) #tail che si può rimuovere per fare in modo che usi uno spazio O(1) e non O(n)

def somma_artim(n, t):
    if n > t:
        return 0

    quantita = t - n + 1
    return quantita * (n + t) // 2

print(somma_notail(2, 98))
print(somma_tail(100,200))
print(somma_artim(100,200))
