#ano de nascimento
repetir = "s"
while repetir == "s":
    idade = int(input("Qual a tua idade? "))
    mes = int(input("Você nasceu em que mês? "))
    anoatual = 2023
    mesatual = int(input("Qual mês atual?"))
    ano = anoatual-idade
    if mes > mesatual:
        ano = ano -1
        print(f"Você nasceu em {ano}")
    else:
        print(f"Você nasceu em {ano}")

    repetir = input("Que fazer novamente? s/n ")
print("valeu!")