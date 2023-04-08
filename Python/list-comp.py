no1 = int(input())
no2 = int(input())
no3 = int(input())
noesp = int(input())
dalist = [
    [a, b ,c]
    for a in range (no1 + 1)
    for b in range (no2 + 1)
    for c in range (no3 + 1)
    if a + b + c !=noesp



]
print(dalist)