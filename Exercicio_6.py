print("Por favor, digite dois números inteiros.")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}. A diferença entre os dois é: {num1 - num2}")
elif num1 == num2:
    print("Os dois números são iguais.")
else:
    print(f"{num2} é maior que {num1}. A diferença entre os dois é: {num2 - num1}")
