import random


num = input("digite um numero inteiro: ")
if num.isnumeric():
    if int(num) % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
else:
    print("digite somente numeros")

