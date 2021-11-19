print("FECHAMENTO DE PEDIDO\n")
cod = input("Informe o código do produto escolhido: ")
quant = float(input("Agora, informe a quantidade:"))

match cod:
    case "100":
        print(f"\nO valor a ser pago é o de {1.20 * quant}. Dirija-se ao caixa. Obrigada!")
    case "101":
        print(f"\nO valor a ser pago é o de {1.30 * quant}. Dirija-se ao caixa. Obrigada!")
    case "102":
        print(f"\nO valor a ser pago é o de {1.50 * quant}. Dirija-se ao caixa. Obrigada!")
    case "103":
        print(f"\nO valor a ser pago é o de {1.20 * quant}. Dirija-se ao caixa. Obrigada!")
    case "104":
        print(f"\nO valor a ser pago é o de {1.70 * quant}. Dirija-se ao caixa. Obrigada!")
    case "105":
        print(f"\nO valor a ser pago é o de {2.20 * quant}. Dirija-se ao caixa. Obrigada!")
    case "106":
        print(f"\nO valor a ser pago é o de {1.00 * quant}. Dirija-se ao caixa. Obrigada!")
    case _:
        print("Código de produto não encontrado. Tente novamente!")
