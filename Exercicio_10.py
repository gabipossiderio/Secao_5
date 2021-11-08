print("CALCULE SEU PESO IDEAL (que nem é tão ideal assim, afinal, você pesa o quanto quiser!)")
altura = float(input("Insira sua altura em metros: "))
sexo = (input("Insira sua sexo biológico (Masculino ou Feminino): ".title()))

if sexo == "Masculino":
    print(f"Seu peso ideal é {(72.7 * altura) - 58}.")
else:
    print(f"Seu peso ideal é {(62.1 * altura) - 44.7}.")

print("\nIGNORE OS PADRÕES!! SEJA FELIZ!!")
