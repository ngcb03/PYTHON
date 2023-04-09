"""
Programador: Nicolas G. Camargo B.


Programa: Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.

Por ejemplo si el operador carga un 2 y un 4 significa que debemos crear una lista similar a:

lista=[[1,1,1,1], [1,1,1,1]]


Última modificación: 23-02-23

"""
# Solicitamos componentes y n elementos para componentes lista
comp_lista=int(input("Cantidad de componentes para lista: "))
elementos_comp=int(input("Cantidad de elementos para componentes: "))
print("----------")

# Asignamos compontes para lista
lista=[]
sumaGen=0

# Asignamos elementos para componentes listas
for k in range(comp_lista):
  lista.append([1,1,1,1])
  for x in range(elementos_comp):
    sumaGen+=lista[k][x]

# Listamos la lista
print(lista)
print("Suma elementos lista:",sumaGen)
print("----------")