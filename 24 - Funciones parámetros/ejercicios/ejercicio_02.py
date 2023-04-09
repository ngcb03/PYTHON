"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

Última modificación: 13-03-23

"""

def carga_enteros():
  lista_enteros=[]
  cont=0
  while cont<3:
    lista_enteros.append(int(input("Ingrese entero: ")))
    cont+=1
  print("Lista registrada:",lista_enteros)
  print(); order_descendente(lista_enteros)

def order_descendente(lista_enteros):
  for k in range(len(lista_enteros)-1):
    for f in range(len(lista_enteros)-1):
      if lista_enteros[f]>lista_enteros[f+1]:
        aux=lista_enteros[f]
        lista_enteros[f]=lista_enteros[f+1]
        lista_enteros[f+1]=aux
  print(lista_enteros)

carga_enteros()