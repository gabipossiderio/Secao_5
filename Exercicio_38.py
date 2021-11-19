dia, mes, ano = input("Informe sua data de nascimento. Use o formato DD/MM/AAAA: ").split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes == 2 and ano <= 2021:
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        if 1 <= dia <= 29:
            print("\nData válida.")

    elif 1 <= dia <= 28:
        print("\nData válida.")

    else:
        print("Data inválida.")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if ano <= 2021:
        if 1 <= dia <= 31:
            print("\nData válida.")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if ano <= 2021:
        if 1 <= dia <= 30:
            print("\nData válida.")

else:
    print("\nData inválida.")
