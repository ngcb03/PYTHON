"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
Sumar todos los valores de las listas.

Última modificación: 23-02-23

"""
# definimos lista
lista=[[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]
sumaGen=0

for k in range(len(lista)):  
  for x in range(len(lista[k])):
    sumaGen+=lista[k][x]

print("Suma elementos componentes lista:",sumaGen)