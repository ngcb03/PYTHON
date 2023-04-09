# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
# de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

supMay=0
n = int(input("Cantidad de pares de datos a regitrar: "))
print()

for f in range(n):
  
  print("Triangulo #",f+1)
  base = int(input("Ingrese base -> "))
  altura = int(input("Ingrese altura -> "))
  
  superficie=(base*altura)/2
  print("Superficie ->",superficie)
  print()
  
  if superficie>=12:
    supMay+=1

print("Los triangulos con superficies mayores a 12 son",supMay)