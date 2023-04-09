"""
Programador: Nicolas G. Camargo B.

Programa: En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

Última modificación: 02-02-23

"""
listaEstudiantes = []
listaNotas = []
cont = 0

print("¡Registro datos estudiantes!")
print()

while cont < 5:
  print("Estudiante #",cont+1)
  listaEstudiantes.append(input("Ingrese nombre: "))
  listaNotas.append(float(input("Ingrese nota: ")))
  print()
  cont+=1

print()
notaSup = 0 # Estudiantes con la condición: Muy bueno

for x in range(5):
  print("Esdiante:",listaEstudiantes[x])
  print("Nota:",listaNotas[x])
  if listaNotas[x]>=8:
    print("Condición: Muy Bueno")
    notaSup+=1
  elif listaNotas[x]>=4 and listaNotas[x]<=7:
    print("Condición: Bueno")
  else:
    print("Condición: Insuficiente")

print()
print("Estudiante con condición 'Muy Bueno':",notaSup)