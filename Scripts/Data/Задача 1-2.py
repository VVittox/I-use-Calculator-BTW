import math
def calc_simple():
	n1 = int(input("Введите первое число: "))
	n2 = int(input("Введите второе число: "))
	s = input("Введите операцию: ")
	if s == "+":
		print(n1+n2)
	elif s == "-":
		print(n1-n2)
	elif s == "*":
		print(n1*n2)
	elif s == "/":
		if n2 == 0:
			print("Делить на 0 нельзя.")
		else:
		    print(n1/n2)
def calc_extended():
	choice = int(input("Какую операцию хотите выполнить: 1 - возведение в степень, 2 - остаток от деления, 3 - нахождение корня "))
	if choice == 1:
		n1 = int(input("Введите первое число: "))
		n2 = int(input("Введите второе число: "))
		print(n1**n2)
	elif choice == 2:
		n1 = int(input("Введите первое число: "))
		n2 = int(input("Введите второе число: "))
		if n2 == 0:
			print("Делить на 0 нельзя.")
		else:
		    print(n1%n2)
	elif choice == 3:
		n1 = int(input("Введите число: "))
		print(math.sqrt(n1))
def main():
    calc_extended()

if __name__ == '__main__':
    main()