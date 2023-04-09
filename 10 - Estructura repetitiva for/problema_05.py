# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen 
# notas mayores o iguales a 7 y cuántos menores.

notasMay=0
notasMen=0

for x in range(10):
  nota = int(input("Ingrese valor -> "))
  if nota>=7:
    notasMay+=1
  else:
    notasMen+=1

print("Cantidad de aprobados ->",notasMay)
print("Cantidad de reprobados ->",notasMen)