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
        return calc_10_2(n)
    elif choice == "2":
        n = int(input("Введите число  в 10 СС: "))
        return calc_10_16(n)
    elif choice == "3":
        n = int(input("Введите число  в 10 СС: "))
        return calc_10_8(n)
    else:
        print("Неверный выбор.")
def main():
    res = menu_logic()
    if res is not None:
        print("Результат:", res)

if name == "main":
    main()