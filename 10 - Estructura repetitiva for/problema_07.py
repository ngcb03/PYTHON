# Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o 
# iguales a 1000 (n se carga por teclado)
# Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo 
# primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. 
# Dicha variable se carga antes de entrar a la estructura repetitiva for.

numMay=0
n = int(input("Cantidad valores ingresar -> "))

for x in range(n):
  num = int(input("Ingrese valor -> "))
  if num>=1000:
    numMay+=1

print("La cantidad de valores mayores o iguales a 1000 es",numMay)