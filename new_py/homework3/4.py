def minimum(a):
    min_nim = a[0]
    for i in range(len(a)):
        if a[i] < min_nim:
            min_nim = a[i]
    return print(min_nim)


minimum([4, 8, 9, 6, 30])
