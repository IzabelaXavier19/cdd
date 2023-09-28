repetir = "S"
while repetir == "S":
    nota1 = int(input("Digite sua nota da 1º avaliação: "))
    while nota1<0 or nota1>10:
        nota1 = int(input("Nota invalida! Digite sua nota da 1º avaliação: "))

    nota2 = int(input("Digite sua nota da 2º avaliação: "))
    while nota2<0 or nota2>10:
        nota2 = int(input("Digite sua nota da 2º avaliação: "))

    media = nota1+nota2/2

    print(f"Sua media é {media}")
    repetir = input("Deseja fazer um novo calculo:")
else:
    print("programa encerrado")
