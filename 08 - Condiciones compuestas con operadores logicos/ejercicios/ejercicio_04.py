# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma 
# del primero con el segundo y a este resultado se lo multiplica por el tercero.

num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))
if num1==num2 and num2==num3:
	resultado = (num1+num2)*num3
	print("(num1+num2)*3 ->",resultado)
else:
	print("¡Los valores ingresados NO son todos iguales!")

