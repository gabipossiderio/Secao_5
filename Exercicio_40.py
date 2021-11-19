print("CÁLCULO DE VALOR - CARRO 0KM\n")

custo = float(input("Insira o valor de fábrica do carro desejado: \n"))

if custo < 12000:
    print(f"O carro custará o valor de R${custo * 1.05}.")

elif 12.000 <= custo <= 25000:
    print(f"O carro custará o valor de R${custo * 1.25}.")

else:
    print(f"O carro custará o valor de R${custo * 1.35}.")
