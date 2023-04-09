"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.

Última modificación: 23-02-23

"""
# definimos listas con sus componentes
lista=[[1,3,5,7,9],[2,4,6,8,10]]

# Forma #1
suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
print("Suma elementos componente #1:",suma1)
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print("Suma elementos componente #1:",suma2)
print("----------")

# Forma #2
# sumar elementos x componete de lista
sumaComp1=0 # Suma elementos componente #1
sumaComp2=0 # Suma elementos componente #1
cont=0

while cont<5:
  sumaComp1+=lista[0][cont]
  sumaComp2+=lista[1][cont]
  cont+=1

print("Suma elementos componente #1:",sumaComp1)
print("Suma elementos componente #2:",sumaComp2)
print("----------")

# Forma #3
for k in range(len(lista)):
  suma=0
  for x in range(len(lista[k])):
    suma+=lista[k][x]
  print("Suma elementos componente #",k+1,":",sumaComp1)