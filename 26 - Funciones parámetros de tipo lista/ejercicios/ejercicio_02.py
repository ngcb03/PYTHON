"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))


Última modificación: 13-04-23

"""
# funciones
def mascaracteres(palabras):
  mayorPalabra = palabras[0]
  for f in range(len(palabras)-1):
    if len(mayorPalabra)<len(palabras[f+1]):
      mayorPalabra=palabras[f+1]
    elif len(mayorPalabra)==len(palabras[f+1]):
      print(palabras[f])
      mayorPalabra=palabras[palabras.index(palabras[f])]
  return mayorPalabra


# instrucciones complementarias
palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))