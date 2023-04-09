"""
Programador: Nicolas G. Camargo B.

Programa: Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

Última modificación: 01-02-23

"""

listaEnteros = []
entMayor = 0
cont = 0

while cont<5:
  listaEnteros.append(int(input("Ingrese valor entero: ")))
  cont+=1

entMayor = listaEnteros[0]
for x in range(5):
  if listaEnteros[x]>entMayor:
    entMayor = listaEnteros[x]

print("Lista valores enteros:",listaEnteros)
print("Valor enteros mayor:",entMayor)
