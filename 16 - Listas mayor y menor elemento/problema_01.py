"""
Programador: Nicolas G. Camargo B.

Programa: Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

Última modificación: 29-01-23

"""

listaEnteros = []
may = 1 # guardará posición valor mayor de la lista

print("Registrar enteros:")
for f in range(5):
  listaEnteros.append(int(input("Ingrese valor entero: ")))

print()
print("Lista enteros registrador:",listaEnteros)

for i in listaEnteros:
  for j in listaEnteros:
    if i!=j:
      if i>j:
        may+=1
  if may==5:
    print("Entero mayor lista:",i)
    break;
  else:
    may=1
