print("Informe os coeficientes da equação do segundo grau. Use o formato: ax² + bx + c = 0.")
a = float(input("a:"))

if a != 0:
    b = float(input("b:"))
    c = float(input("c:"))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existe raíz real.")
    elif delta == 0:
        print(f"As raízes são iguais.\nX' = X\" = {- b / (2 * a)}.")
    else:
        print(f"As raízes são diferentes.\n"
              f"X' = {(- b + delta ** 0.5) / (2 * a)}\n"
              f"X\" = {(- b - delta ** 0.5) / (2 * a)}")
else:
    print("Não é uma equação do segundo grau.")
