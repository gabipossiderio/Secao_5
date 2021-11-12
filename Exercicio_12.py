import math

num = int(input("Digite um numero inteiro:"))

if 0 > num:
    print("Numero inválido!")
else:
    print(f"{math.log(num)}")
