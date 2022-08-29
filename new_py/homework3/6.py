def digit_number(x):
    res = 0
    for i in range(len(str(x))):
        res += 1
    return res


print('Количество цифр в числе 123456 = ', digit_number(123456))
