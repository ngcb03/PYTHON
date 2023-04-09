# Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
# Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el 
# enunciado del problema.

print("¡Sumador progresivo de números enteros!")

suma=0 # Variable encargada que guardar la suma de los valores ingresados
sl=0 # Variable comprobar para salida

while sl==0: # Condición para seguir digitando
  numEnt = int(input("Ingrese valor entero: "))
  suma+=numEnt
  if numEnt==(-1):
    sl=1 # Parar de ingresar datos
    print()
    print("¡Hasta pronto!")
  else:  
    print("Nota -> Para salir digite -1")
