"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos.

Última modificación: 05-03-23

"""
# Detallamos las funciones
def recString(oracion):
  listaVocales=['a','e','i','o','u']
  cont_vocales=0
  
  for k in oracion:
    for f in listaVocales:
      if k==f:
        cont_vocales+=1
  return cont_vocales


cont=0
while cont<3:
  print("Cantidad vocales:",recString(input("Ingrese oración: ")))
  print(); cont+=1

print("¡Programa terminado!")