print("CÁLCULO DE APOSENTADORIA")
idade = int(input("Insira sua idade: "))
tempo = int(input("Insira o tempo de contribuição: "))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print("Você já pode se aposentar.")

else:
    print("Que pena! Você ainda não pode se aposentar.")
