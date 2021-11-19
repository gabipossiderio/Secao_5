print("PROVA DE MATEMÁTICA - 2° ANO - PROFESSORA GABRIELLA")
nome_do_aluno = input("\nAluno (a): ")
pergunta_1 = int(input("\nQuestão 01 - Quanto é 10 + 17? "))
pergunta_2 = int(input("\nQuestão 02 - Quanto é 52 + 8? "))
pergunta_3 = int(input("\nQuestão 03 - Quanto é 46 + 14? "))
pergunta_4 = int(input("\nQuestão 04 - Quanto é 83 + 11? "))
pergunta_5 = int(input("\nQuestão 05 - Quanto é 41 + 25? "))

print("\nGABARITO")
print("\nQuestão 01 - R: 27"
      "\nQuestão 02 - R: 60"
      "\nQuestão 03 - R: 60"
      "\nQuestão 04 - R: 94"
      "\nQuestão 05 - R: 66")

numero_acertos = 0

if pergunta_1 == 27:
    numero_acertos += 1
if pergunta_2 == 60:
    numero_acertos += 1
if pergunta_3 == 60:
    numero_acertos += 1
if pergunta_4 == 94:
    numero_acertos += 1
if pergunta_5 == 66:
    numero_acertos += 1

print(f"\nVocê acertou {numero_acertos} questões.")
