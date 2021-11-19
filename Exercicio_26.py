print("VERIFICAÇÃO DE ECONOMIA DO VEÍCULO \n")
km = float(input("Digite a quantidade de KMs a ser percorrida: "))
litro = float(input("Digite a quantidade de litros a ser consumida: "))
consumo = (km / litro)

if consumo < 8:
    print("\nVENDA O CARRO!")

elif 8 >= consumo >= 14:
    print("\nEconômico!")

else:
    print("\nSuper econômico!")
