def task(start, fin):
    p = 1
    for i in range(min(start, fin), max(start, fin) + 1):
        p *= i
    return p


print(task(int(input("верхняя граница=")), int(input("нижняя граница="))))
