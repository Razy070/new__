def polindrom(x):
    comp = ''.join(reversed(str(x)))
    return str(x) == str(comp)


num = 7809  # ввести число
if polindrom(num):
    print('Число ', num, '- полиндром.')
else:
    print('Число ', num, '- не полиндром.')
