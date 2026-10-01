def long_multiply():
    try:
        num1 = input("Введите первое число: ").strip()
        num2 = int(input("Введите второе число: ").strip())
        
        int(num1)
        
        if num2 == 0:
            print("Нельзя делить на ноль!")
            return
        if num1 == "0":
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
        print("Ошибка: Вводить можно только целые числа, остальные символы недопустимы)!")