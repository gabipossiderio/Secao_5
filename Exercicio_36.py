print("CÁLCULO DE COMISSÃO")
valor = float(input("Informe o valor mensal vendido pelo vendendor em reais:"))

if valor >= 100_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {700 + 0.16 * valor}")
elif 80_000 <= valor < 100_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {650 + 0.14 * valor}")
elif 80_000 <= valor < 100_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {600 + 0.14 * valor}")
elif 60_000 <= valor < 80_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {550 + 0.14 * valor}")
elif 40_000 <= valor < 60_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {500 + 0.14 * valor}")
elif 20_000 <= valor < 40_000:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {450 + 0.14 * valor}")
else:
    print(f"O valor da comissão a ser paga ao vendedor é de R$ {400 + 0.14 * valor}")
