"""
Programador: Nicolas G. Camargo B.

Programa: Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.
Ingresar los siguientes valores por teclado: 1200, 750, 820, 550 y 490

Última modificación: 02-02-23

Nota: Se hace uso del método la burbuja para el intercambio de valores

"""
listaSueldos = []
cont = 0

print("¡Registro de sueldos!")
while cont<5:
  print("Empleado #",cont+1)
  listaSueldos.append(float(input("Ingrese sueldo: ")))
  cont+=1
  print()

# Comparar compontes de la lista sucesivamente 
for x in range(4): # Si la lista tiene N componentes hay que hacer N-1 comparaciones.
  if listaSueldos[x]>listaSueldos[x+1]:
    aux = listaSueldos[x+1]
    listaSueldos[x+1] = listaSueldos[x]
    listaSueldos[x] = aux

# Comparar componentes con última
"""
for x in range(5):
  if listaSueldos[x]>listaSueldos[len(listaSueldos)-1]:
    aux=listaSueldos[len(listaSueldos)-1]
    listaSueldos[len(listaSueldos)-1]=listaSueldos[x]
    listaSueldos[x]=aux
"""

print("Lista valor mayor al final:",listaSueldos)