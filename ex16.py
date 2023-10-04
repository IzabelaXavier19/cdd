maca = 0
qtd = int(input("Quantas maçãs você vai levar hoje? "))

if qtd < 12:
    maca = 1.30 * qtd
  
else:
    maca = 1.00 * qtd
print(f"Total foi: R${maca} Volte sempre! ")
  
