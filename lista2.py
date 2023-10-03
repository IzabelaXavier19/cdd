notas = [0,0,0,0,0]
soma = 0
for x in range(5):
    notas[x] = float(input(f"Digite sua {x+1} nota: "))

for i in range(5):
    soma += notas[i]
media = soma/5

for y in range(5):
    if notas[y]>=media:
        print(notas[y])






