"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.

Última modificación: 13-04-23

"""
# funciones
def cargaEnteros():
  listaEnteros = []
  cont = 0
  while cont<5:
    listaEnteros.append(int(input("Ingrese valor entero: ")))
    cont+=1
  print()
  return listaEnteros

def mayorDiez(listaEnteros):
  for f in listaEnteros:
    if f>10:
      print(f)


# bloque principal del programa
mayorDiez(cargaEnteros())