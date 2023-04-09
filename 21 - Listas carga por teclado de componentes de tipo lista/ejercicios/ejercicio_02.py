"""
Programador: Nicolas G. Camargo B.


Programa: Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.


Última modificación: 03-03-23

"""
nombres_empleados=["Nicolas Camargo","Daniel Jimenez","Camilo Gonzalez"]
dias_faltaron=[[5,17],[26],[]]

# listamos empleados y dias que faltaron
for x in range(len(nombres_empleados)):
  print("Empleado:",nombres_empleados[x])
  print("Dias que faltó:",dias_faltaron[x])
  print("Cantidad inasistencias:",len(dias_faltaron[x]))
  print()

# empleado con menos faltas
menor=len(dias_faltaron[x])
poscMenor=0
for k in range(len(dias_faltaron)-1):
  if len(dias_faltaron[k])>len(dias_faltaron[k+1]):
    menor=len(dias_faltaron[k+1])
    poscMenor=k+1

print("Empleado con menos faltas:",nombres_empleados[poscMenor])
print("Dias faltó:",menor)