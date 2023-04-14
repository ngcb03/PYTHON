"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

Última modificación: 13-04-23

"""
# funciones
def cargaEnteros():
  listaEnteros = []
  cont = 0
  while cont<5:
    listaEnteros.append(int(input("Ingrese valor entero: ")))
    cont+=1
  return listaEnteros

def menMay(lista):
  menMay = [lista[0],lista[0]] # indices: 0 -> menor y 1 -> mayor
  for f in range(1,len(lista)):
    if menMay[0]>lista[f]:
      menMay[0]=lista[f]
    else:
      if menMay[1]<lista[f]:
        menMay[1]=lista[f]
  print("El menor valor de la lista es",menMay[0])
  print("El mayor valor de la lista es",menMay[1])


# bloque principal
menMay(cargaEnteros())