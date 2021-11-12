print("CÁLCULO DE NOTA FINAL(Insira suas notas de 0 à 10).")
num1 = float(input("Digite a nota do Trabalho de Laboratório: "))

if num1 < 0 or num1 > 10:
    print("Nota de Trabalho de Laboratório Inválida!")
else:
    num2 = float(input("Digite a nota da Avaliação Semestral: "))
    if num2 < 0 or num2 > 10:
        print("Nota de Trabalho de Avaliação Simestral Inválida!")
    else:
        num3 = float(input("Digite a nota do Exame Final: "))
        if num3 < 0 or num3 > 10:
            print("Nota de Trabalho de Exame Final Inválida!")
        else:
            media_ponderada = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10
            if 0 <= media_ponderada <= 2.9:
                print(f"A sua média ponderada é {media_ponderada}. Que pena! Você foi reprovado.")
            elif 3 <= media_ponderada <= 4.9:
                print(f"A sua média ponderada é {media_ponderada}. Você está de recuperação!")
            else:
                print(f"A sua média ponderada é {media_ponderada}. Parabéns! Você está aprovado!")
