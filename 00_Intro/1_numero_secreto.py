print("Introduce un número")

cadena_numero = input()
numero = int(cadena_numero)

secreto = 8

if numero == secreto :
	print("Enhorabuena acertastes el numero secreto")
else :
	if numero < secreto : 
		print("El numero secreto es mayor")
	else :
		print("el numero secreto es menor")
