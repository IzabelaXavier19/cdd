idade = int(input("Qual a sua idade: "))
meses = int(input("Quantos meses: "))
dias = int(input("Quantos dias: "))

ano = idade*365
mes = meses*30
dia = ano+mes+dias

print(f"Você está com {dia} vividos")
