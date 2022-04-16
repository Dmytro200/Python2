
text1 = input(f"Виберіть одну з операцій (+, -, *, /):")

text2 = input("Введіть перше число:")

text3 = input("Введіть друге число:")

print(int(text2))
print(int(text3))

if text1 == '+':
    print(f"{int(text2)}+{int(text3)}={int(text2) + int(text3)}")

elif text1 == '-':
    print(f"{int(text2)}-{int(text3)}={int(text2) - int(text3)}")

elif text1 == '*':
    print(f"{int(text2)}*{int(text3)}={int(text2) * int(text3)}")

elif text1 == '/':
    print(f"{int(text2)}/{int(text3)}={int(text2) / int(text3)}")

else:
    print("Невірний символ(((")



