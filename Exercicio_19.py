numero = int(input("Informe um número inteiro, será retornado se ele é divisível por 3 e/ou por 5:"))

if numero % 3 == 0 and numero % 5 == 0:
    print("É divisível por ambos.")
elif numero % 3 != 0 and numero % 5 != 0:
    print("Não é divisível nem por 3 e nem por 5.")
elif numero % 3 != 0 and numero % 5 == 0:
    print("Não é divisível por 3.")
    print("É divisível por 5.")
else:
    print("É divisível por 3.")
    print("Não é divisível por 5.")
