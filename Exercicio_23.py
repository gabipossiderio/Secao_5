ano = int(input("Insira um ano para descobrir se ele é bissexto: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano informado é bissexto.")

else:
    print("O ano informado não é bissexto.")
