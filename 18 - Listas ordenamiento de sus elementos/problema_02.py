"""
Programador: Nicolas G. Camargo B.

Programa: Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

Última modificación: 02-02-23

"""

listaSueldos = []
cont = 0

print("¡Registro sueldo empleados!")
while cont<5:
  print("Empleado #",cont+1)
  listaSueldos.append(float(input("Ingrese sueldo: ")))
  cont+=1

# Método de la burbuja | forma N-1
for k in range(4):
  for x in range(4):
    if listaSueldos[x]>listaSueldos[x+1]:
      aux=listaSueldos[x]
      listaSueldos[x]=listaSueldos[x+1]
      listaSueldos[x+1]=aux

print()
print("Lista ordenada:")
print(listaSueldos)
