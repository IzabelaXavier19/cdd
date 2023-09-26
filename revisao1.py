#media
resp = "s"

while resp == "s" or "S":
    num1 = float(input("Digite a primeira nota: "))
    num2 = float(input("Digite a primeira nota: "))
    media = num1 + num2 / 2

    if media >=7:

        print(f"APROVADO sua media é: ", media)
    elif media >=4:
        print(f"RECUPERAÇÃO sua media é: ",media)
    else:
        print(f"Foto com proff SAUDADES!!",media)

    resp = input("Quer continuar: s/n ")

    print("valeu")