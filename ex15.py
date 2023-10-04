inicio = int(input("Informe a hora inicial: "))
fim = int(input("Informe a hora final: "))
hora = fim - inicio
if inicio>fim:
    hora+=24
    print(hora)
else:
    print(hora)
