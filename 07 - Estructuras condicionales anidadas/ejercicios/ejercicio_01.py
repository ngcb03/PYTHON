# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos

num1 = int(input("Ingresa primer valor: "))
num2 = int(input("Ingresa segundo valor: "))
num3 = int(input("Ingresa tercer valor: "))
print("El valor mayor es")
if num1>num2:
  if num1>num3:
    print(num1)
  else:
    print(num3)  
else:    
  if num2>num3:
    print(num2)    
  else:
    print(num3)  