#positivo e negativo diferente de zero
resp = "s"
while resp == "s" or resp == "S":
    num = int(input("Digite um numero: "))
    while num == 0:
        print("numero invalido!")
        num = int(input("Digite um numero: "))
    if num < 0:
        print("Negativo")
    else:
        print("Positivo")

    resp = input("Deseja continuar: s/n ")

print("tchau!")



