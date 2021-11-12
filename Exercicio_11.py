numero = input("Informe um número inteiro maior que zero: ")

quantidade_caracteres = len(numero)
condicao = int(numero)
soma = 0

if condicao > 0:
    for i in range(0, quantidade_caracteres):
        soma += int(numero[i])
    print(f"A soma de seus algarismos é {soma}.")
else:
    print("Número inválido.")
