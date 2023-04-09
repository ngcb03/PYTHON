"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

Última modificación: 01.02.23

"""

listaNombres = []
listaEdades = []
listaAux = []
cont = 0

print("Registro personas:")
print()

while cont < 5:
  print("Persona #",cont+1)
  listaNombres.append(input("Ingresa nombre: "))
  listaEdades.append(int(input("Ingresa edad: ")))
  if listaEdades[cont]>=18:
    listaAux.append(cont)
  cont+=1

print()
print("Personas mayores de edad:")
for f in listaAux:
  print(listaNombres[f])
