"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

Última modificación: 04-03-23

"""
# definimos lista enteros
lista_enteros=[]
aux_lista=[]
x=0

# registramos valores enteros
print("Registro valores enteros!")
for k in range(10):
  print("Registro valor #",k+1)
  lista_enteros.append(int(input("Ingrese valor:: ")))
  aux_lista.append(lista_enteros[k])
  print()
  
  if aux_lista[x]==5:
    aux_lista.pop(x)
    # Otra forma de eliminar elementos de una lista: del(aux_lista[x])
    x-=1
  x+=1

# listamos lista total
print(lista_enteros)
print()

# listamos lista eliminando valores igules a 5
print(aux_lista)
print()
