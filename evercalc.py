#evercalc by evercode
#Version v1.0

#Вопрос (без подвоха)
what = input("Выберите действие (+, -): ")

a = float( input("Введите первое число: "))
b = float( input("Введите второе число: "))

if what == "+":
    c = a + b
    print("Результат" +  str(c))
elif what == "-":
    c = a - b
    print("Результат" +  str(c))
else:
    print("Неверное действие")
