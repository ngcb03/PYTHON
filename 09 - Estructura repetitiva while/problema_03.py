# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre 
# posteriormente la suma de los valores ingresados y su promedio.

contador=0
num=0
suma=0
while contador<10:
  print("Valor #",contador+1)
  num=int(input("Ingresa un valor -> "))
  print()
  suma+=num
  contador+=1
print("La suma de los 10 valores es ->",suma)
prom=suma/10
print("El promedio de los 10 valores es ->",prom)