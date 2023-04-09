"""
Programador: Nicolas G. Camargo B.

Programa: Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

Última modificación: 02-02-23

"""

listaEnt1 = []
listaEnt2 = []
sumaListas = []
cont = 0

print("¡Registro de valores enteros!")
while cont < 4:
  print("Valor #",cont+1)
  listaEnt1.append(int(input("Ingrese primer valor entero: ")))
  listaEnt2.append(int(input("Ingrese segundo valor entero: ")))
  print()
  cont+=1

for x in range(4):
  sumaListas.append(listaEnt1[x]+listaEnt2[x])

print()
print("Suma paralela listas enteros:",sumaListas)
