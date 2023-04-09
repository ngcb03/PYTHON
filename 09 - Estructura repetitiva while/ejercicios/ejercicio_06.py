# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar
#  con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes 
# "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

i=0
j=0
lista1=0
lista2=0

while i<2:
  print("Lista #",i+1)
  while j<15:
    valor = int(input("Ingresar valor: "))
    if i==0:
      lista1+=valor
    else:
      lista2+=valor
    j+=1
  i+=1
  j=0
  print()

if lista1==lista2:
  print("¡Listas iguales!")
else:
  if lista1>lista2:
    print("¡Lista 1 mayor!")  
  else:
    print("¡Lista 2 mayor!")  