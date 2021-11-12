print("CÁLCULO DE NOTA FINAL(Insira suas notas de 0 à 10).")
num1 = float(input("Digite a nota do Trabalho de Laboratório: "))
num2 = float(input("Digite a nota da Avaliação Semestral: "))
num3 = float(input("Digite a nota do Exame Final: "))
media_ponderada = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10

if 0 <= media_ponderada <= 2.9:
    print(f"A sua média ponderada é {media_ponderada}. Que pena! Você foi reprovado.")

elif 3 <= media_ponderada <= 4.9:
    print(f"A sua média ponderada é {med

elif 3 <= media_ponderada <= 4.9:
    print(f"A sua média ponderada é {media_ponderada}. Você está de recuperação!")

else:
    print(f"A sua média ponderada é {media_ponderada}. Parabéns! Você está aprovado!")
