print("EMPRÉSTIMO CONSIGNADO")
salario = float(input("Digite seu salário mensal: "))
emprestimo = float(input("Digite o valor da prestação do empréstimo: "))

if salario * 0.2 >= emprestimo:
    print("Empréstimo concedido com sucesso.")
else:
    print("Infelizmente não será possível conceder seu empréstimo.")
