def long_add():
    try:
        num1 = input("Введите первое число: ").strip()
        num2 = input("Введите второе число: ").strip()

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
        
            sum = d1 + d2 + exc
            res.append(sum % 10)
            exc = sum // 10
        
        if exc:
            res.append(exc)
        
        res_str = "".join(str(i) for i in reversed(res))
        print(res_str)

    except ValueError:
        print("Ошибка: Вводить можно только целые числа, остальные символы недопустимы)!")