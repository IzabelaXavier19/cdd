repetir = "s"
while repetir == "s":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))

    if num1>num2:
        if num1>num3:
            print(f"O maior é {num1}")
    elif num3<num2:
            print(f"numero {num2} ")
    else:
        print(f"o maior é {num3}")

    repetir = input("Deseja fazer novamente? s/n ")
print("valeu!")