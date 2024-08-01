import random

Epar = True

while Epar:
    num = input("digite um numero inteiro: ")
    if num == "break":
        Epar = False
        break

    if num.isnumeric():
        if int(num) % 2 == 0:
            print(f"{num} é par")
        else:
            print(f"{num} é impar")
    else:
        print("digite somente numeros")

