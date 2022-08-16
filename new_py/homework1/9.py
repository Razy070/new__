from math import sqrt

print("1-треугольник")
figure = input("Выберите фигуру:")


def string(param):
    pass


if figure == '1':
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь: %.2f" % s)
