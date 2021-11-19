print("CALCULE SEU IMC\n")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura ** 2
print(f"Seu IMC é {imc}.")

if imc <= 18.5:
    print("Magreza leve.")
elif 18.6 <= imc <= 24.9:
    print("Saudável.")
elif 25.0 <= imc <= 29.9:
    print("Peso em excesso.")
elif 30.0 <= imc < 34.9:
    print("Obesidade Grau I")
elif 35.0 <= imc < 39.9:
    print("Obesidade Grau II (severa).")
else:
    print("Obesidade Grau III (mórbida).")
