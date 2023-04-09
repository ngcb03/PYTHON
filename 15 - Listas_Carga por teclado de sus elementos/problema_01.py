# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado 
# y añadirlos a la lista. Imprimir la lista generada.

listaEnteros = [] # lista vacía
cont = 0 # contador buble

while cont<5:
  listaEnteros.append(int(input("Ingrese valor entero: ")))
  cont+=1

print(listaEnteros)