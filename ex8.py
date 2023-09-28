num1 = 0
soma = 0
qtd = int(input("Quantos numeros vc quer soma: "))
for x in range(qtd):
    num1 = int(input("Dgite um numero: "))
    soma += num1

media = soma/qtd
print(f"A soma é {soma} e a media {media}")