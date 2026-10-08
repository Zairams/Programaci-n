print("Introduce un número y mostrare su tabla correspondiente")
cadena_numero = input()
numero = int(cadena_numero)

print("Dime otro numero")
cadena_numero2 = input()
numero2 = int(cadena_numero2)


while (numero2 <= 10 ) :
	result = numero * numero2
	print( numero , "x" , numero2 , "=" , result )
	numero2 = numero2 + 1	
