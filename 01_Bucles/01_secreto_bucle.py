print("Introduce un númer9o")

cadena_numero = input()
numero = int(cadena_numero)

secreto = 8

'''
if numero == secreto :
	print("Enhorabuena acertastes el numero secreto")
else :
	print("No has acertado")
'''

while True:
	print("Introduce un número")

	cadena_numero = input()
	numero = int(cadena_numero)
	
	if numero == secreto :
		print("Enhorabuena acertastes el numero secreto")
	else :
		print("No has acertado")	






'''
	if numero < secreto : 
		print("El numero secreto es mayor")
	else :
		print("el numero secreto es menor")


print("Dime otro numero, a ver si esta aciertas")
numero2 = int(input())

secreto = 8

if numero2 != secreto :
	if (numero2 < numero) and (numero < secreto) :
		print("Has introducido un número más pequeño todavia")

	if (numero2 > numero) and (numero > secreto) :
		print("Has introducido un numero más grande todavia")

	if (numero2 > numero) and (numero < secreto) : 
		print("Fallaste, pero al menos me has hecho caso, has ido a más")
	if (numero2 < numero) and (numero > secreto) :
		print("Has fallado pero has hecho caso y reducido")
	if numero2 == secreto :
		print("Has acertado, muy bien")
	
'''	
