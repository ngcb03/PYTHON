"""
Programador: Nicolas G. Camargo B.

Programa: Se tiene la siguiente lista:lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista.

Última modificación: 23-02-23

"""
# definimos lista
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

# listamos lista
print(lista)
print("----------")

for k in range(len(lista)):
  for x in range(len(lista[k])):
    if lista[k][x]>10:
      lista[k][x]=0

# listamos lista
print(lista)
print("----------")