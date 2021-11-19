print("VERIFICAÇÃO DE CATEGORIA\n")

idade = int(input("Insira a idade do nadador (a partir de 5 anos): "))

if idade < 5:
    print("Idade inválida. Tente novamente!")

elif 5 <= idade <= 7:
    print("Sua categoria é: Infantil A.")

elif 8 <= idade <= 10:
    print("Sua categoria é: Infantil B.")

elif 11 <= idade <= 13:
    print("Sua categoria é: Juvenil A.")

elif 14 <= idade <= 17:
    print("Sua categoria é: Juvenil B.")

else:
    print("Sua categoria é: Sênior.")

print("\nProcure a secretaria para efetuar sua matrícula!")
