"""
Programador: Nicolas G. Camargo B.


Programa: Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

En este problema definiremos tres listas:

Una lista para almacenar los nombres de los empleados, por ejemplo si lo cargamos por asignación:

nombres=["juan", "ana", "luis"]

Una lista paralela a la anterior para almacenar los sueldos en los últimos tres meses por cada empleado:

sueldos=[[5000,5100,5000], [7000,6500,6000], [2500,2500,2500]]

Otra lista paralela donde almacenamos el total de sueldos cobrados por cada empleado que resulta de sumar los tres sueldos de cada empleado contenidos en la lista sueldos:

totalsueldos=[15100, 19500, 7500]

Es importante notar que estos datos no los cargaremos por asignación sino los cargaremos por teclado a las dos primeras listas y la tercera la generaremos extrayendo los datos de la lista sueldos.


Última modificación: 23-02-23

"""

# definimos listas
empleados = []
sueldos = []

# cargar información empleados

print("¡Registro empleados!")
for x in range(3):
  print("Empleados #",x+1)
  empleados.append(input("Ingrese nombre: "))
  sueldos.append([float(input("Ingrese primer sueldo: ")),float(input("Ingrese segundo sueldo: ")),float(input("Ingrese tercer sueldo: "))])
  print()

# Total sueldos cobrados
totalsueldos=[]
aux=0

for k in range(3):
  for x in range(3):
    aux+=sueldos[k][x]
  totalsueldos.append([aux])
  aux=0

# Listamos sueldos acumulados
print("Sueldos acumulados últimos 3 meses:")
print(empleados,":",totalsueldos)
print()

#### MI SOLUCIÓN ####

# Llenamos lista con valores independientes
aux_totalsueldos=[]
for k in range(len(totalsueldos)):
    aux_totalsueldos.append([totalsueldos[k][0]])

# Empleado con mayor sueldo
for k in range(len(aux_totalsueldos)-1):
  for x in range(len(aux_totalsueldos)-1):
    if aux_totalsueldos[x][0]>=aux_totalsueldos[x+1][0]:
      aux=aux_totalsueldos[x][0]
      aux_totalsueldos[x][0]=aux_totalsueldos[x+1][0]
      aux_totalsueldos[x+1][0]=aux

empleado_mayor_sueldo=totalsueldos.index([24.0])
print("Empleado mayor sueldo acumulado:",empleados[empleado_mayor_sueldo])
print()

#### SOLUCION PLANTEADA GUIA ####

posmayor=0
mayor=totalsueldos[0]
for x in range(1,3):
    if totalsueldos[x]>mayor:
        mayor=totalsueldos[x]
        posmayor=x

print("Empleado con mayores ingresos en los ultimos tres meses",empleados[posmayor],"con un ingreso de",mayor)