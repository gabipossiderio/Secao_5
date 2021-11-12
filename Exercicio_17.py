base_maior = float(input("Insira o tamanho da base maior do trapézio: "))

if base_maior <= 0:
    print("Número inválido! Insira um valor maior que 0.")

else:
    base_menor = float(input("Insira o tamanho da base menor do trapézio: "))
    if base_menor <= 0:
        print("Número inválido! Insira um valor maior que 0.")
    else:
        altura = float(input("Insira o tamanho da altura do trapézio: "))
        if altura <= 0:
            print("Número inválido! Insira um valor maior que 0.")
        else:
            print(f"A área do trapézio é igual a {(base_maior + base_menor) * altura / 2}")
