def menu_numbers():
    print("1. Простые операции")
    print("2. Расширенные операции")
    print("3. Тригонометрические действия с градусами")
    print("4. Тригонометрические действия с радианами")
    print("5. Логические операции")
    print("6. Перевод чисел в различные СС")
    print("7. Проверка скобок")

    a = int(input("Выберите действие: "))

    if a == 1:
        calc_simple()
    elif a == 2:
        calc_extended()
    elif a == 3:
        calc_degrees()
    elif a == 4:
        calc_radians()
    elif a == 5:
        calc_logic()
    elif a == 6:
        menu_logic()
    elif a == 7:
        check_brackets()