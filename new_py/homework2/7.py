for i in range(int(input("Первое число: ")), int(input("Второе число: ")) + 1): print(
    'Fizz Buzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)