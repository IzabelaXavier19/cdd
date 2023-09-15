#for x in  range(0,10,1)
#for (x=1;x<10;x++)

soma = 0
for x in  range(10):
    num = float(input("Digite um número: "))
    soma = soma +num
print(soma)

n = 0
for x in range(10):
    num = int(input("Digite um numero: "))

    if n < 0:
        n = n + 1
        print(n)