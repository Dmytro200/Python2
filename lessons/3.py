text = input("Введіть ім'я користувача:")

print(f"Привіт, {text.title()}!")

text1 = input("Введіть перше число:")
print(int(text1))

text2 = input("Введіть друге число:")
print(int(text2))

if int(text1) > int(text2):
    print(f"\n{int(text1)} > {int(text2)} \nПерше число більше другого.")
elif int(text1) == int(text2):
    print(f"\n{int(text1)} = {int(text2)} \nЧисла рівні між собою.")
elif int(text1) < int(text2):
    print(f"\n{int(text1)} < {int(text2)} \nДруге число більше першого.")




