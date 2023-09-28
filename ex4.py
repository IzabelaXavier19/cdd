num1 = int(input("Digite um primeiro numero: "))
num2 = int(input("Digite um primeiro numero: "))
num3 = int(input("Digite um primeiro numero: "))

if num1 >num2:
    if num1>num3:
        print(f"O maior é {num1}")
    else:
        print(f"O maior é {num3}")
elif num2 >num3:
    print(f"O maior é {num2}")
else:
    print(f"O maior é {num3}")
