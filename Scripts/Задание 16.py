def menu_strings():
    print("1. Простые операции со строками")
    print("2. Вывод строки по центру экрана")
    print("3. Количество слов и количество уникальных слов")
    print("4. Статистика по символам строки")

    a = int(input("Выберите действие: "))

    if a == 1:
        str_simple()
    elif a == 2:
        str_showcenter()
    elif a == 3:
        str_words()
    elif a == 4:
        str_stat()