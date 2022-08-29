def draw_square(n, s, f):
    r = s * n
    if not f:
        m = s + " " * (n - 2) + s
    else:
        m = r
    print(r)
    for i in range(n - 2):
        print(m)
    print(r)


draw_square(5, "#", True)
print("")
draw_square(5, "*", False)


