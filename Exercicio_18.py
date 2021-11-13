print("OPERAÇÕES MATEMÁTICAS \n")
print("Observe a tabela abaixo e digite a letra de acordo com a operação matemática desejada: \n"
      "A - Adição (+)\n"
      "B - Subtração (-)\n"
      "C - Multiplicação (*)\n"
      "D - Divisão (/)\n")

op = (input("Operação escolhida: ")).title()

if op != "A" and op != "B" and op != "C" and op != "D":
    print("Operação inválida! Tente novamente.")

else:
    print("Agora, insira os números da operação: ")

    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    match op:
        case "A":
            print(num1 + num2)
        case "B":
            print(num1 - num2)
        case "C":
            print(num1 * num2)
        case _:
            print(num1 / num2)
