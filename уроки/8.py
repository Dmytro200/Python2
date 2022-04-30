text1 = input("Виберіть одну з операцій (+, -, *, /, +++):")

numbers = []
total = 0

if text1 == '+++':

    text = None
    while text != '':
        text = input("Введіть число и напишите Enter (якщо бажаете завершити, просто напишите Enter):")
        if text != '':
            numbers.append(int(text))
    print(sum(numbers))

elif text1 == '+':
    text2 = input("Введіть перше число:")

    text3 = input("Введіть друге число:")

    print(f"{int(text2)}+{int(text3)}={int(text2) + int(text3)}")

elif text1 == '-':
    text2 = input("Введіть перше число:")

    text3 = input("Введіть друге число:")

    print(f"{int(text2)}-{int(text3)}={int(text2) - int(text3)}")

elif text1 == '*':
    text2 = input("Введіть перше число:")

    text3 = input("Введіть друге число:")

    print(f"{int(text2)}*{int(text3)}={int(text2) * int(text3)}")

elif text1 == '/':
    text2 = input("Введіть перше число:")

    text3 = input("Введіть друге число:")

    if int(text3) == 0:
         try:
             text3 = 0
         except IndexError:
             text3 = ''
         finally:
             print('На ноль делить нельзя')

    else:
         print(f"{int(text2)}/{int(text3)}={int(text2) / int(text3)}")

else:
    print("Невірний символ(((")

