"""
Programador: Nicolas G. Camargo B.

Programa: Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

Última modificación: 10-02-23

"""

listaEnteros = [542323,356,7012,1232,9123]

for i in range(4):
  for j in range(4):
    if listaEnteros[j]>listaEnteros[j+1]:
      aux=listaEnteros[j+1]
      listaEnteros[j+1]=listaEnteros[j]
      listaEnteros[j]=aux

print("Lista enteros menor-mayor:",listaEnteros)

for i in range(4):
  for j in range(4):
    if listaEnteros[j]<listaEnteros[j+1]:
      aux=listaEnteros[j+1]
      listaEnteros[j+1]=listaEnteros[j]
      listaEnteros[j]=aux

print("Lista enteros mayor-menor:",listaEnteros)