"""
Programador: Nicolas G. Camargo B.

Programa: Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.

Última modificación: 10-02-23

"""

empleados=int(input("Ingrese cantidad empleados: "))
sueldos = []
cont = 0

while cont < empleados:
  print("Empleado #",cont+1)
  sueldos.append(float(input("Ingrese sueldo: ")))
  print()
  cont+=1

for i in range(empleados-1):
  for j in range(empleados-1):
    if sueldos[j]>sueldos[j+1]:
      aux=sueldos[j+1]
      sueldos[j+1]=sueldos[j]
      sueldos[j]=aux

print("Sueldos ordenados:",sueldos)