n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
while n1 == n2:
  n2 = int(input("INVALIDO, Digite outro numero: "))
if n1>n2:
  print(f"Em ordem crescente: {n2},{n1}")
else:
  print(f"Em ordem crescente: {n1},{n2}")
