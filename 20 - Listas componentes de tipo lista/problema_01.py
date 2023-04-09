"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.

Última modificación: 20-02-23

"""
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print(lista)
print("---------")
# imprimimos la primer componente
print(lista[0])
print("---------")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("---------")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
  print(lista[0][x])
print("---------")

for f in range(4):
  print("Componente lista #",f+1)
  for k in range(3):
    print(lista[f][k])