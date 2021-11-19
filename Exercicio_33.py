print("CÁLCULO DE AJUSTE DE PREÇO")
preco = float(input("\nInsira o valor do produto em reais: "))

if preco <= 50:
    preco += 0.05 * preco
    print(f"\nO preço atualizado é: R$ {preco}")

elif 50 < preco <= 100:
    preco += 0.1 * preco
    print(f"\nO preço atualizado é: R$ {preco}")

else:
    preco += 0.15 * preco
    print(f"\nO preço atualizado é: R${preco}")

if preco <= 80:
    print("\nO produto está barato.")
elif 80 < preco <= 120:
    print("\nO produto está normal.")
elif 120 < preco <= 200:
    print("\nO produto está caro.")
else:
    print("\nO produto está muito caro.")
