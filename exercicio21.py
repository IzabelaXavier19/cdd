senhav = "2222"
senha = input("Qual é a senha: ")
tent = 1
while senha != senhav:
    if tent >=3:
        print("Senha bloqueada")
        break
    senha = input("Senha incorreta! Qual é a senha: ")
    tent += 1
else:
    print("Senha correta")
