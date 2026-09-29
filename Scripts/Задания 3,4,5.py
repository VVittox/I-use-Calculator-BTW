import math



# Задание 3: Тригонометрический калькулятор в градусах
def calc_degrees():
    choice = int(input("Введите номер действия (1 – sin(), 2 – cos()): "))
    angle_deg = int(input("Введите угол в градусах: "))
    
    # Переводим градусы в радианы для библиотеки math без не не посчитаются синус и косинус
    angle_rad = math.radians(angle_deg)
    
    if choice == 1:
        print(f"Результат: {math.sin(angle_rad)}")
    elif choice == 2:
        print(f"Результат: {math.cos(angle_rad)}")
    else:
        print("Неверный номер действия.")


# Задание 4: Тригонометрический калькулятор (радианы)
def calc_radians():
    choice = int(input("Введите номер действия (1 – sin(), 2 – cos()): "))
    angle_rad = float(input("Введите угол в радианах: "))
    
    if choice == 1:
        print(f"Результат: {math.sin(angle_rad)}")
    elif choice == 2:
        print(f"Результат: {math.cos(angle_rad)}")
    else:
        print("Неверный номер действия.")


# Задание 5: Калькулятор логических величин
def calc_logic():
    choice = int(input("Введите номер действия (1 – and, 2 – or, 3 – not): "))
    
    if choice in (1, 2):
        # Для and / or вводим два значения
        val1 = bool(int(input("Введите первое значение (0 - False, 1 - True): ")))
        val2 = bool(int(input("Введите второе значение (0 - False, 1 - True): ")))
        if choice == 1:
            print(f"Результат: {val1 and val2}")
        else:
            print(f"Результат: {val1 or val2}")
    elif choice == 3:
        # Для not вводим одно значение
        val = bool(int(input("Введите значение (0 - False, 1 - True): ")))
        print(f"Результат: {not val}")
    else:
        print("Неверный номер действия.")

