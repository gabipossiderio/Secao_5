print("Por favor, digite dois números:")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num2} é maior que {num1}.")
else:
    print(f"Os dois números são iguais.")
