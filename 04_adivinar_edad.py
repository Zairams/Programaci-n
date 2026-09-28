print("Introduce el año de nacimiento")
cadena_nacimiento = input()
nacimiento = int(cadena_nacimiento)

print("Año actual")
cadena_actual = input()
actual = int(cadena_actual)

edad_actual = actual - nacimiento
print("Tienes", edad_actual, "años")

if edad_actual >= 18 :
	print("Eres mayor de edad")

else:
	print("Eres menor de edad")
	




