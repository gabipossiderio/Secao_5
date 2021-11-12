print("DIAS DA SEMANA")
num1 = input("Insira um número inteiro de 1 à 7 para receber um dia da semana: ")

match num1:
    case "1":
        print("Domingo")
    case "2":
        print("Segunda-feira")
    case "3":
        print("Terça-feira")
    case "4":
        print("Quarta-feira")
    case "5":
        print("Quinta-feira")
    case "6":
        print("Sexta-feira")
    case "7":
        print("Sábado")
    case _:
        print("Dia da semana não encontrado!")
