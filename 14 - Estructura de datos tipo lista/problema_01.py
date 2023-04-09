# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

listaEnt = [1,3,5,7,9]
sumaGen = 0 # Guarda suma enteros de la lista
cont = 0 # Contador

while cont<len(listaEnt):
  sumaGen+=listaEnt[cont]
  cont+=1

print("Suma lista enteros:",sumaGen)