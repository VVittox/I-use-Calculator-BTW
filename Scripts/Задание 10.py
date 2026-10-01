def proverka_skobok():
    txt = input("Введите строку с формулой: ")

    s = 0

    for i in txt:
        if i == "(":
            s += 1
        elif i == ")":
            s -= 1

            if s < 0:
                print("НЕТ")
                return

    if s == 0:
        print("ДА")
    else:
        print("НЕТ")