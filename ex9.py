n = int(input("Digite um numero: "))
menu = int(input("Digite 1 para antecessor ou 2 para Sucessor"))
ant = n - 1
suc = n + 1
if menu == 1:
    if n < 0:
        ant = n - (-1)
    ant = n - 1
    print(f"Seu antecessor é {ant}")
elif menu == 2:
    if n<0:
        suc = n - 1
    suc = n + 1
    print(f"Seu sucessor {suc}")
else:
    print("Programa encerrado")
print(f"Seu sucessor {suc} e seu antecessor é {ant}")
