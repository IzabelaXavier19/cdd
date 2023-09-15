neg = 0
soma = 0
positivo =0
for x in range(10):
    num = int(input("digite um numero: "))
    if num < 0:
        neg = neg + 1
        soma = soma + num
        print(num)
        positivo = 10 - neg
print(f"a quantidade de numeros negativos é {neg}, e a soma é {soma} e positivos são {positivo}")