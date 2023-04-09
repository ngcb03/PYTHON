# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos
# valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna
# el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

contador=0
pares=0
impares=0

numCargar = int(input("Cantidad de números a registrar: "))

while contador<numCargar:
  valor = int(input("Ingresar valor: "))
  if valor%2==0:
    pares+=1
  else:
    impares+=1
  contador+=1

print("La cantidad de valores pares es",pares)
print("La cantidad de valores impares es",impares)