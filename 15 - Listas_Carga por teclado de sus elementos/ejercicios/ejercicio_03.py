"""
Programador: Nicolas G. Camargo B.

Programa: Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
  (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los 
  sueldos de los empleados agrupados en dos listas.
  Imprimir las dos listas de sueldos.

Última modificación: 29-01-23

"""
sueldoMan = []
sueldoTar = []

print("¡Turno mañana!")
for f in range(4):
  sueldoMan.append(float(input("Ingrese sueldo: ")))
print()
print("¡Turno tarde!")
for f in range(4):
  sueldoTar.append(float(input("Ingrese sueldo: ")))

print()
print("Sueldos empleados mañana:",sueldoMan)
print("Sueldos empleados tarde:",sueldoTar)