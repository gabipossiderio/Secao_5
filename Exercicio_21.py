print("MENU DE OPÇÕES \n"
      "1 - Soma de 2 números \n"
      "2 - Diferença entre 2 números (insira primeiro o maior) \n"
      "3 - Produto entre 2 números \n"
      "4 - Divisão entre 2 números (o denominador não pode ser zero \n")

opcao = int(input("Insira a opção desejada: "))

if 1 <= opcao <= 4:
  print("Agora, insira os números da operação.")

  num1 = float(input("Insira o primeiro número: "))
  num2 = float(input("Insira o segundo número: "))

  match opcao:
      case "1":
          print(f"O resultado da operação é {num1 + num2}.")
      case "2":
          print(f"O resultado da operação é {(num1 - num2).__abs__()}.")
      case "3":
          print(f"O resultado da operação é {num1 * num2}.")
      case _:
          if num2 != 0:
              print(f"O resultado da operação é {num1 / num2}.")
          else:
              print("O denominador deve ser diferente de zero!")
else:
    print("Opção inválidada. Tente novamente.")
