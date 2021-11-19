print("Informe 3 números para recebê-los em ordem crescente:\n")
numeros = [int(input("Número 1: ")), int(input("Número 2: ")), int(input("Número 3: "))]

numeros.sort()

print(f"\n{numeros[0]} - {numeros[1]} - {numeros[2]}")
