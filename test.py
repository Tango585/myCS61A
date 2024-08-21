def hailstone(n):
    k: int = n
    i = 1
    print(k)
    while k != 1:
        if k % 2 == 0:
            k = k // 2
            print(k)
            i += 1
        else:
            k = 3 * k + 1
            print(k)
            i += 1
    return i
a=hailstone(27)
print(a)