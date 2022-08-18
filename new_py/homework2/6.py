d = [str(i) for i in range(int(input()), int(input()) + 1)]
print(' '.join(d))
print(' '.join(d[::-1]))
print(' '.join([i for i in d if int(i) % 7 == 0]))
print(len([i for i in d if int(i) % 5 == 0]))
