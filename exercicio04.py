n = input("Qual seu nome: ")
idade = int(input("Sua idade? "))
salario = float(input("Seu salario? "))
percentual = float(input("Qual é o percentual do aumento? "))
filhos =int(input("Quantos filhos você tem? "))


aumento = salario/100 * percentual


salariocomaumento = salario + aumento
salariofamilia = 150 * filhos
abonoferias = salariocomaumento/3

#15% desconto de renda e inss 8%

ir= salariocomaumento/100 * 15
inss= salariocomaumento/100 * 8

descontoir = salariocomaumento - ir
descontoinss =salariocomaumento - inss

salariototal = (salariocomaumento + abonoferias) - descontoinss - descontoir + salariofamilia
print(f"Olá, {n}, tem {idade} anos, seu salário é {salario} , novo salario {salariocomaumento}, salario familia {salariofamilia}, abono ferias {abonoferias}, sobrou isso {salariototal}")
