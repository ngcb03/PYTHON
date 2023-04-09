"""
Programador: Nicolas G. Camargo B.

Programa: Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

Última modificación: 04-03-23

"""
# definimos listas
nombres_empleados=[]
sueldos_empleados=[]

# cantidad empleados a registrar
n_empleados=int(input("Cantidad de empleados: "))

# ingresamos valores a listas
for k in range(n_empleados):
  print("EMPLEADO #",k+1)
  nombres_empleados.append(input("Ingrese nombre: "))
  sueldos_empleados.append(float(input("Ingrese sueldo: ")))
  print()

# listamos empleados y sueldos que le corresponde a cada uno
print(nombres_empleados)
print(sueldos_empleados)
print()

# eliminamos eempleados con sueldo mayor a 10000
x=0
for f in range(n_empleados):
  if sueldos_empleados[x]>10000:
    nombres_empleados.pop(x)
    sueldos_empleados.pop(x)
    x-=1
  x+=1

print(nombres_empleados)
print(sueldos_empleados)
print()