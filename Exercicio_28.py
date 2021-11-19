print("Escolha uma opção de cálculo de média:\n"
      "1 - Média geométrica\n"
      "2 - Média ponderada (peso 1, 2 e 3, respectivamente)\n"
      "3 - Média harmônica\n"
      "4 - Média aritmética")
opcao = int(input("Opção: "))

if 1 <= opcao <= 4:
    numero_1 = float(input("Número 1:"))
    numero_2 = float(input("Número 2:"))
    numero_3 = float(input("Número 3:"))

    match opcao:
        case 1:
            print(f"Média geométrica: {(numero_1 * numero_2 * numero_3) ** 3}")
        case 2:
            print(f"Média ponderada: {(numero_1 + 2 * numero_2 + 3 * numero_3) / 6}")
        case 3:
            print(f"Média harmônica: {(numero_1 ** -1 + numero_2 ** -1 + numero_3 ** -1) ** -1}")
        case _:
            print(f"Média aritmética: {(numero_1 + numero_2 + numero_3) / 3}")
else:
    print("Opção inválida!")
