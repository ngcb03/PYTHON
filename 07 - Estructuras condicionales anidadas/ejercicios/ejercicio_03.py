# Confeccionar un programa que permita cargar un número entero positivo de hasta tres
# cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje
# de error si el número de cifras es mayor.

numEntero = int(input("Ingresa un valor entero: "))
cifras=0
if numEntero>0:
  if numEntero<1000:
    if numEntero>99:
      cifras=3
    else:
      if numEntero>9:
        cifras=2
      else:
        cifras=1
else:
  if numEntero>(-1000):
    if numEntero>(-100):
      if numEntero>(-10):
        cifras=1
      else:
        cifras=2
    else:
      cifras=3    

if cifras>0:
  print("Cifras del valor ingresado:",cifras)
else:
  print("¡El valor cuenta con más de 3 cifras!")              