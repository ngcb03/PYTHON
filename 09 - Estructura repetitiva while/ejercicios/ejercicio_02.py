# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura 
# promedio de las personas.

contador=0
sumaAlt=0

n = int(input("Cantidad de alturas a registrar: "))

while contador<n:
  print("Altura para persona #",contador+1)
  altura = float(input("Ingresa altura: "))
  sumaAlt+=altura
  contador+=1

promAltura=(sumaAlt/n)
print("El promedio de las alturas registradas es",promAltura)