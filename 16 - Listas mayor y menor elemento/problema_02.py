"""
Programador: Nicolas G. Camargo B.

Programa: Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

Última modificación: 29-01-23

"""
listaEnteros = []
cont = 0
menorEnt = 0
posicion = 0

while cont < 5:
  listaEnteros.append(int(input("Ingrese entero: ")))
  cont+=1

menorEnt = listaEnteros[0]
for f in range(1,5):
  if listaEnteros[f] < menorEnt:
    menorEnt = listaEnteros[f]
    posicion = f

print("Lista completa:",listaEnteros)
print("Menor lista enteros:",menorEnt)
print("Posición del menor en la lista:",posicion)