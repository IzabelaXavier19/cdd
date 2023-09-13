hora1= int(input("Digite a hora: "))
min1= int(input("e quantos minutos: "))
hora2= int(input("Digite a hora: "))
min2= int(input("e quantos min: "))
htemp = 0

if hora1 >12:
    h1 = hora1-12
if hora2 >12:
    h2 = hora2-12

totalmin = min1+min2

if totalmin >= 60:
    totalmin -= 60
    htemp = 1

horat = hora1 + hora2 + htemp
if horat >12:
    horat = horat -12

print(f"hora {horat}:{totalmin}")

#entrada01 = 3:45
#entrada02 = 14:20

# 6:05