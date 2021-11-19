print("BOLETIM DO ALUNO")

nota = float(input("\nInsira sua nota: "))
falta = int(input("Insira seu número de faltas: "))

if 0 <= nota <= 3.9 or (4.0 <= nota <= 4.9 and falta > 20):
    print("\nSeu conceito é: E.")

elif 4.0 <= nota <= 4.9 or (5.0 <= nota <= 7.4 and falta > 20):
    print("\nSeu conceito é D.")

elif 5.0 <= nota <= 7.4 or (7.5 <= nota <= 8.9 and falta > 20):
    print("\nSeu conceito é C.")

elif 7.5 <= nota <= 8.9 or (9.0 <= nota <= 10 and falta > 20):
    print("\nSeu conceito é B.")

elif 9 <= nota <= 10:
    print("\nSeu conceito é A.")

else:
    print("\nNota inválida. Tente novamente!")
