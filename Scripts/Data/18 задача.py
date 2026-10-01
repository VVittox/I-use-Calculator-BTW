def long_sub():
    try:
        num1 = input("Введите первое число: ").strip()
        num2 = input("Введите второе число: ").strip()
        
        # Валидация на отсутствие букв
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
        print("Ошибка: Вводить можно только целые числа, остальные символы недопустимы)!")