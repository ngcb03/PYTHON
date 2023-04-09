# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos 
# valores almacenan un valor superior a 100.

listaEnteros = [23,104,34,342,89,201,8,78]
mayCien = 0

for f in listaEnteros:
  if f>100:
    mayCien+=1

print("Cantidad valores mayores a 100:",mayCien)