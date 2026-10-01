import string

def str_simple():
    print("Введите строку с операцией: (+ или *): ")
    ch = input()
    if ch == '+':
        print("Введите первую строку: ")
        str1 = input()
        print("Введите вторую строку: ")
        str2 = input()
        print(f"Результат: {str1 + str2}")

    elif ch == '*':
        print("Введите строку: ")
        str1 = input()
        print("Введите число: ")
        n = input()
        if n.isdigit():
            n = int(n)
            print(f"Результат: {str1 * n}")
        else:
            print("Неверный ввод.")

    else:
        print("Неверная операция.")

def str_showcenter(): 
    width = 80
    height = 25
    print("Введите строку: ")
    str1 = input()
    top_padding = height // 2
    print("\n" * top_padding, end="")
    print(str1.center(width))

def str_words():
    print("Введите строку: ")
    str1 = input()
    words = str1.split()
    unique_count = len(set(words))
    print(f"Количество слов: {len(words)}")
    print(f"Количество уникальных слов: {unique_count}")

def str_stat():
    print("Введите строку: ")
    str1 = input()
    lenght = len(str1)
    numbers = sum(c.isdigit() for c in str1)
    uppercase = sum(c.isupper() for c in str1)
    lowercase = sum(c.islower() for c in str1)
    spaces = sum(c.isspace() for c in str1)
    print(f"Длина строки: {lenght}")
    print(f"Количество цифр: {numbers}")
    print(f"Количество заглавных букв: {uppercase}")
    print(f"Количество строчных букв: {lowercase}")
    print(f"Количество пробелов: {spaces}")
