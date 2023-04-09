"""
Programador: Nicolas G. Camargo B.

Programa: Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

Última modificación: 20-03-23

"""
# declaramos funciones
def prom_enteros(lista_enteros):
  prom=0
  for f in lista_enteros:
    prom+=f
  return (prom/3)

# complemento
cont=0
lista_enteros=[]

while cont<3:
  print("Registro entero #",cont+1)
  lista_enteros.append(int(input("Ingrese valor entero:")))
  cont+=1

print(prom_enteros(lista_enteros))