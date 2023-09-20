
valor1 = int(input("Digite um numero: "))
valor2 = int(input("Digite outro numero: "))
cont = 0
while valor2 == 0:
    valor2 = int(input("Numero invalido! Digite outro numero: "))
    cont +=1
    if cont > 4:
        print("maior que 5 tentativas")
        break


div = valor1/valor2
print(div)

