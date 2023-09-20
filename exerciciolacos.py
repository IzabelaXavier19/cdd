x = 0
soma = 0

qtd = int(input("Quantos tem: "))
while x < qtd:
    valores = float(input("Digite um valor: "))
    soma = soma + valores
    x+=1

media = soma/qtd
print(media)