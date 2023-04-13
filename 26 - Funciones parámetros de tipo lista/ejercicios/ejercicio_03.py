"""
Programador: Nicolas G. Camargo B.

Programa: Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa. 


Última modificación: 13-04-23

"""
# funciones
def producto(listaEnteros):
  producto = 1
  for f in listaEnteros:
    producto *= f
  return producto


# instrucciones complementarias
enteros = [5,4,3,2,1]
print("producto elementos lista:" , producto(enteros))