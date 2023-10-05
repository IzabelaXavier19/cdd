from bibli
resp = 0

while repetir == "s":
    menu = print("""
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir """)

    opcao = input("Escolha uma opção: ")

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if opcao == "1":
        somar(num1,num2)
    elif opcao == "2":
        dividir(num1,num2)
    elif opcao == "3":
        multiplicar(num1,num2)
    elif opcao == "4":
        dividir(num1,num2)

    repetir = input("Deseja fazer novamente: s/n")
print("Valeu!!")