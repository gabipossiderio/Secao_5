print("CÁLCULO DE IMPOSTO \n")
print("Observe a tabela abaixo para calcular seu imposto: \n"
      "MG = 7% \n"
      "SP = 12% \n"
      "RJ = 15% \n"
      "MS = 8% \n")

estado = input("Insira o estado do destino do produto: ").upper()

if estado == "RJ" or estado == "SP" or estado == "RJ" or estado == "MG" or estado == "MS":
    valor = float(input("Insira o valor do produto: "))

    match estado:
      case "MG":
          print(f"O preço final acrescido do imposto é {valor + (valor * 0.07)}")
      case "SP":
          print(f"O preço final acrescido do imposto é {valor + (valor * 0.12)}")
      case "RJ":
          print(f"O preço final acrescido do imposto é {valor + (valor * 0.15)}")
      case _:
          print(f"O preço final acrescido do imposto é {valor + (valor * 0.08)}")
else:
  print("Estado inválido. Tente novamente!")
