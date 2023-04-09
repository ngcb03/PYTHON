"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor debemos intercambiar los nombres para que las listas continúen paralelas (es decir que en los mismos subíndices de cada lista continúe la información relacionada)

Última modificación: 10-02-23

"""
alumnos = []
notas = []
cont = 0

print("¡Registro notas estudiantes!")
while cont < 5:
  print("Alumno #",cont+1)
  alumnos.append(input("Nombre completo: "))
  notas.append(float(input("Nota: ")))
  print()
  cont+=1

print(len(alumnos)-1)

# Método de la burbuja para ordenamiento de listas de la forma N-1
for i in range(len(alumnos)-1):
  for j in range(len(alumnos)-1):
    if notas[j]<notas[j+1]: # mayor a menor
      
      # mantener paralelas listas
      
      ## cambio de notas
      aux=notas[j+1]
      notas[j+1]=notas[j]
      notas[j]=aux
      
      ## cambio de alumnos
      aux=alumnos[j+1]
      alumnos[j+1]=alumnos[j]
      alumnos[j]=aux

print("¡Estudiantes ordenados nota mayor-menor!")
for f in range(5):
  print(alumnos[f],"-",notas[f])