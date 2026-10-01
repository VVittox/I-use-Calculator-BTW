import math


def calc_simple():
    n1 = int(input("Введите число 1: "))
    n2 = int(input("Введите число 2: "))
    operation = input("Введите операцию +,-,/,* : ")

    if operation == "+":
        print(n1 + n2)
    elif operation == "-":
        print(n1 - n2)
    elif operation == "*":
        print(n1 * n2)
    elif operation == "/":
        if n2 == 0:
            print("Делить на 0 нельзя великий математик.")
        else:
            print(n1 / n2)


def calc_extended():
    choice = int(input(
        "Какую операцию хотите выполнить: "
        "1 - возведение в степень, 2 - остаток от деления, "
        "3 - нахождение корня: "
    ))

    if choice == 1:
        n1 = int(input("Введите число 1: "))
        n2 = int(input("Введите число 2: "))
        print(n1 ** n2)
    elif choice == 2:
        n1 = int(input("Введите число 1: "))
        n2 = int(input("Введите число 2: "))
        if n2 == 0:
            print("Делить на 0 нельзя математик.")
        else:
            print(n1 % n2)
    elif choice == 3:
        n1 = int(input("Введите число: "))
        print(math.sqrt(n1))


def calc_degrees():
    choice = int(input("Введите номер действия (1  sin(), 2  cos()): "))
    angle_deg = int(input("Введите угол в градусах: "))
    angle_rad = math.radians(angle_deg)

    if choice == 1:
        print(f"Результат: {math.sin(angle_rad)}")
    elif choice == 2:
        print(f"Результат: {math.cos(angle_rad)}")
    else:
        print("Неверный номер действия.")


def calc_radians():
    choice = int(input("Введите номер действия (1  sin(), 2  cos()): "))
    angle_rad = float(input("Введите угол в радианах: "))

    if choice == 1:
        print(f"Результат: {math.sin(angle_rad)}")
    elif choice == 2:
        print(f"Результат: {math.cos(angle_rad)}")
    else:
        print("Неверный номер действия.")


def calc_logic():
    choice = int(input("Введите номер действия (1  and, 2  or, 3  not): "))

    if choice in (1, 2):
        val1 = bool(int(input(
            "Введите 1 значение (0 False, 1  True): "
        )))
        val2 = bool(int(input(
            "Введите 2 значение (0  False, 1  True): "
        )))
        if choice == 1:
            print(f"Результат: {val1 and val2}")
        else:
            print(f"Результат: {val1 or val2}")
    elif choice == 3:
        val = bool(int(input("Введите значение (0  False, 1  True): ")))
        print(f"Результат: {not val}")
    else:
        print("Неверный номер действия.")


def calc_10_2(n):
    return bin(n)[2:]


def calc_10_8(n):
    return oct(n)[2:]


def calc_10_16(n):
    return hex(n)[2:]


def menu_logic():
    print("Меню перевода чисел")
    print("1. Перевод числа из 10 СС в 2 СС")
    print("2. Перевод числа из 10 СС в 16 СС")
    print("3. Перевод числа из 10 СС в 8 СС")

    choice = input("Выберите пункт (1-3): ").strip()

    if choice == "1":
        n = int(input("Введите число в 10 СС: "))
        print("Результат:", calc_10_2(n))
    elif choice == "2":
        n = int(input("Введите число в 10 СС: "))
        print("Результат:", calc_10_16(n))
    elif choice == "3":
        n = int(input("Введите число в 10 СС: "))
        print("Результат:", calc_10_8(n))
    else:
        print("Ужасный выбор.")


def check_brackets():
    txt = input("Введите строку с формулой: ")
    s = 0

    for char in txt:
        if char == "(":
            s += 1
        elif char == ")":
            s -= 1
            if s < 0:
                print("НЕТ")
                return

    if s == 0:
        print("ДА")
    else:
        print("НЕТ")


def menu_numbers():
    print("1| Простые операции")
    print("2| Расширенные операции")
    print("3| Тригонометрические действия с градусами")
    print("4| Тригонометрические действия с радианами")
    print("5| Логические операции")
    print("6| Перевод чисел в различные СС")
    print("7| Проверка скобок")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        calc_simple()
    elif choice == 2:
        calc_extended()
    elif choice == 3:
        calc_degrees()
    elif choice == 4:
        calc_radians()
    elif choice == 5:
        calc_logic()
    elif choice == 6:
        menu_logic()
    elif choice == 7:
        check_brackets()


def str_simple():
    print("Введите строку с операцией: (+ или *): ")
    operation = input()

    if operation == "+":
        print("Введите первую строку: ")
        str1 = input()
        print("Введите вторую строку: ")
        str2 = input()
        print(f"Результат: {str1 + str2}")
    elif operation == "*":
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


def menu_strings():
    print("1| Простые операции со строками")
    print("2| Вывод строки по центру экрана")
    print("3| Количество слов и количество уникальных слов")
    print("4| Статистика по символам строки")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        str_simple()
    elif choice == 2:
        str_showcenter()
    elif choice == 3:
        str_words()
    elif choice == 4:
        str_stat()


def long_add():
    try:
        num1 = input("Введите 1 число: ").strip()
        num2 = input("Введите 2 число: ").strip()

        int(num1)
        int(num2)

        dig1 = [int(i) for i in reversed(num1)]
        dig2 = [int(i) for i in reversed(num2)]

        res = []
        exc = 0
        mx_ln = max(len(dig1), len(dig2))

        for i in range(mx_ln):
            if i < len(dig1):
                d1 = dig1[i]
            else:
                d1 = 0
            if i < len(dig2):
                d2 = dig2[i]
            else:
                d2 = 0

            total = d1 + d2 + exc
            res.append(total % 10)
            exc = total // 10

        if exc:
            res.append(exc)

        res_str = "".join(str(i) for i in reversed(res))
        print(res_str)

    except ValueError:
        print(
            "Ошибка: Вводить можно только целые числа, "
            "остальные символы недопустимы)!"
        )


def long_sub():
    try:
        num1 = input("Введите число 1: ").strip()
        num2 = input("Введите число 2: ").strip()

        int(num1)
        int(num2)

        def is_less(a, b):
            if len(a) != len(b):
                return len(a) < len(b)
            return a < b

        negative = False
        if is_less(num1, num2):
            num1, num2 = num2, num1
            negative = True

        dig1 = [int(i) for i in reversed(num1)]
        dig2 = [int(i) for i in reversed(num2)]

        res = []
        loan = 0

        for i in range(len(dig1)):
            d1 = dig1[i] - loan
            if i < len(dig2):
                d2 = dig2[i]
            else:
                d2 = 0

            if d1 < d2:
                d1 += 10
                loan = 1
            else:
                loan = 0

            res.append(d1 - d2)

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        res_str = "".join(str(i) for i in reversed(res))
        if negative and res_str != "0":
            res_str = "-" + res_str

        print(res_str)

    except ValueError:
        print(
            "Ошибка: Вводить можно только целые числа, "
            "остальные символы недопустимы)"
        )


def long_multiply():
    try:
        num1 = input("Введите 1 число: ").strip()
        num2 = int(input("Введите 2 число: ").strip())

        int(num1)

        if num2 == 0 or num1 == "0":
            print("0")
            return

        dig1 = [int(i) for i in reversed(num1)]
        res = []
        exc = 0

        for i in dig1:
            prod = i * num2 + exc
            res.append(prod % 10)
            exc = prod // 10

        while exc:
            res.append(exc % 10)
            exc //= 10

        res_str = "".join(str(i) for i in reversed(res))
        print(res_str)

    except ValueError:
        print(
            "Ошибка: Вводить можно только целые числа, "
            "остальные символы недопустимы)!"
        )


def menu_long():
    print("Меню длинной арифметики")
    print("1| Сложение")
    print("2| Вычитание")
    print("3| Умножение")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        long_add()
    elif choice == 2:
        long_sub()
    elif choice == 3:
        long_multiply()


def menu():
    print("1| Калькулятор чисел")
    print("2| Калькулятор строк")
    print("3| Длинная арифметика")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        menu_numbers()
    elif choice == 2:
        menu_strings()
    elif choice == 3:
        menu_long()


def main():
    print("Добро пожаловать в *I Use Calculator BTW* от команды I use Arch BTW!")
    menu()


if __name__ == "__main__":
    main()
