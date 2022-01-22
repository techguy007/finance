import math

vklad = input("poc. vklad: ")
ukladani = input("rocni vklad: ")
urok = input("urok: ")
prubezna_castka = int()
soucet = int()

urok = (float(urok)/100) + 1
ukladani = int(ukladani)
vklad = int(vklad)

prubezna_castka = vklad

print("zacatek :",prubezna_castka)

for i in range(100):
	prubezna_castka *= urok
	print(i+1,"rok",prubezna_castka)
	prubezna_castka += ukladani