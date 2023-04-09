# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores

contador=0
notasMay=0
while contador<10:
  print("Nota para estudiante #",contador+1)
  nota = int(input("Ingresa nota: "))
  if nota>=7:
    notasMay+=1
  contador+=1
print("La cantidad de alumnos aprobados es",notasMay)    