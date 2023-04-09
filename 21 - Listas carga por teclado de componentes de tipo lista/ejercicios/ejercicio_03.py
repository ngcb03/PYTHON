"""
Programador: Nicolas G. Camargo B.


Programa: Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]


Última modificación: 03-03-23

"""
lista=[]
aux_lista=[]

# asignamos elementos a la lista
for k in range(50):
  for x in range(k+1):
    aux_lista.append(x+1)
  lista.append(aux_lista)
  aux_lista=[]

print(lista)