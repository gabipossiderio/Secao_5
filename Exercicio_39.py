print("CÁLCULO DE REAJUSTE DE SALÁRIO\n")

salario_atual = float(input("Insira o salário atual: "))
tempo = int(input("Insira quantos ANOS COMPLETOS o funcionário já trabalhou: "))

if tempo < 1:
    bonus = 0
elif 1 <= tempo <= 3:
    bonus = 100
elif 4 <= tempo <= 6:
    bonus = 200
elif 7 <= tempo <= 10:
    bonus = 300
else:
    bonus = 500

if salario_atual <= 500:
    print(f"Seu novo salário é de R${(salario_atual * 1.25) + bonus}.")
elif salario_atual <= 1000:
    print(f"Seu novo salário é de R${(salario_atual * 1.20) + bonus}.")
elif salario_atual <= 1500:
    print(f"Seu novo salário é de R${(salario_atual * 1.15) + bonus}.")
elif salario_atual <= 2000:
    print(f"Seu novo salário é de R${(salario_atual * 1.10) + bonus}.")
else:
    if bonus == 0:
        print(f"Você não possui alteraçôes salariais.")
    else:
        print(f"Seu novo salário é de R${salario_atual + bonus}.")
