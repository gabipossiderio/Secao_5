print("BOLETIM DO ALUNO")
num1 = float(input("Digite uma nota válida (de 0.0 à 10.0): "))
num2 = float(input("Digite mais uma nota válida (de 0.0 à 10.0): "))
num3 = num1 + num2
if 0.0 <= num1 <= 10.0 and 0.0 <= num2 <= 10.0:
    print(f"A média de notas é: {num3 / 2}")
elif not (0.0 <= num1 <= 10.0) and not (0.0 <= num2 <= 10.0):
    print("As duas notas são inválidas. Por favor, tente novamente!")
elif not 0.0 <= num2 <= 10.0:
    print(f"A nota 2 é inválida. Por favor, tente novamente!")
else:
    print("A nota 1 é inválida. Por favor, tente novamente!")
