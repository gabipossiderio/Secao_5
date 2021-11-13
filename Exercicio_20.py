print("INSIRA OS VALORES DOS LADOS DE UM TRIÂNGULO")

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    print("Valores incorretos. Lembre-se: O comprimento de cada lado de um triângulo deve ser menor do que a soma dos"
          " outros dois lados.")
else:
    if (a == b == c):
        print("É um triângulo equilátero pois possui os três lados iguais.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles pois possui dois lados iguais.")
    else:
        print("É um triângulo escaleno pois possui os três lados diferentes.")
