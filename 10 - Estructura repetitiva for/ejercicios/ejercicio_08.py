# Se cuenta con la siguiente información:
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio 
# de edades mayor.

promManiana=0
promTarde=0
promNoche=0

i=0

print("¡Estudiante turno mañana!")
for f in range(22):

  edad = int(input("Ingrese edad -> "))

  if i==0:
    promManiana+=edad
    if f==5:
      i+=1
      print()
      print("¡Estudiantes turno tarde!")
  else:
    if i==1 and f<=10:
      promTarde+=edad
      if f==10:
        i+=1

        print()
        print("¡Estudiantes turno noche!")
    else:
      promNoche+=edad

  #print()
  #print(promManiana)
  #print(promNoche)
  #print(promTarde)
  #print()

promManiana/=6
print("Promedio edades estudiante turno mañana -> ",promManiana)
promTarde/=5
print("Promedio edades estudiante turno tarde -> ",promTarde)
promNoche/=11
print("Promedio edades estudiante turno noche -> ",promNoche)
print()

if promManiana>promTarde and promManiana>promNoche:
  print("¡El turno de MAÑANA tiene el promedio mayor!")
else:
  if promTarde>promManiana and promTarde>promNoche:
    print("¡El turno de TARDE tiene el promedio mayor!")
  else:
    print("¡El turno de NOCHE tiene el promedio mayor!") 