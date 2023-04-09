"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

Última modificación: 05-03-23

"""
# definimos lista
listaEnteros=[]
aux_lista=[] #lista esclava que copia a listaEnteros -> Para eliminación valores >= 10

# cargamos lista con valores enteros
cont=0
x=0

while cont<5:
  print("Registro #",cont+1)
  listaEnteros.append(int(input("Ingrese valor entero:")))
  aux_lista.append(listaEnteros[cont])
  print()
  if aux_lista[x]>=10:
    aux_lista.pop()
    x-=1
  cont+=1
  x+=1

# listamos listas resultantes
print()
print("Lista registrada:",listaEnteros)
print("Lista resultante:",aux_lista)