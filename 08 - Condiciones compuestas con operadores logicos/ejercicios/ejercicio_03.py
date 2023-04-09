# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))
if num1>10 or num2>10 or num3>10:
	print("¡Uno o varios valores son mayores a diez!")
else:
	print("¡Ninguno de los valores es mayor a 10!")

