print("CLASSIFICAÇÃO ")
altura = float(input("Infome sua altura em metros: "))
peso = float(input("Infome seu peso em quilogramas: "))

if altura < 1.2:
    if peso < 60:
        print("Classificação A")
    elif 60 <= peso <= 90:
        print("Classificação D")
    else:
        print("Classificação G")

elif 1.2 <= altura <= 1.7:
    if peso < 60:
        print("Classificação B")
    elif 60 <= peso <= 90:
        print("Classificação E")
    else:
        print("Classificação H")

else:
    if peso < 60:
        print("Classificação C")
    elif 60 <= peso <= 90:
        print("Classificação F")
    else:
        print("Classificação I")
