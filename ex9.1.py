
while True:
    n = int(input("Digite um numero: "))
    menu = input("Digite 1 para antecessor ou 2 para Sucessor ou 3 para os dois: ")
    ant = n - 1
    suc = n + 1
    if menu == "1":
        ant = n - 1
        print(f"Seu antecessor é {ant}")
    elif menu == "2":
        suc = n + 1
        print(f"Seu sucessor {suc}")
    elif menu == "3":
        print("Programa encerrado")
        break