qtd = int(input("Quantos alunos tem na sala: "))
alunos = []
for x in range(qtd):
    alunos.append(input("Qual o nome do aluno: "))
    #alunos[x] = input("Qual o nome do aluno: ")
    #alunos.append()inclue na ultima posicao
for y in range(qtd):
    print(f"Aluno: {alunos[y]}, posição: {y}, seu ranking é : {y+1}")



