# Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.

print("¡VALOR MAYOR DE TRES NUMEROS ENTEROS DIFERENTES!")
num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))
if num1!=num2 and  num2!=num3 and num1!=num3:
	print("El valor mayor es")
	if num1>num2 and num1>num3:
		print(num1)
	else:
		if num2>num1 and num2>num3:
			print(num2)
		else:
			print(num3)
else:
	print("¡Los valores ingresados no son todos distintos!")
