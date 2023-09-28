#Numero diferrente de zero e se é positivo e negativo
rep = "s"
while rep == "s" or rep == "S":
    n = int(input("Digite um numero: "))

    while n == 0:
        n = int(input("Numero invalido!! Digite um numero: "))
    if n < 0:
        print(f"{n} é Negativo")
    else:
        print(f"{n} é Positivo")

    rep = input("Quer fazer novamente: s/n ")
print("Valeu!")