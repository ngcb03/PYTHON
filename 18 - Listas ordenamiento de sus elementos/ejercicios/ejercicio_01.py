"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla

Última modificación: 05-02-23

"""

listaPaises = []
cont = 0

print("¡Registro paises!")
while cont<5:
  print("País #",cont+1)
  listaPaises.append(input("Ingrese pais: "))
  cont+=1

# Método de la burbuja | Forma N-1
for k in range(4):
  for x in range(4):
    ps1 = listaPaises[x]
    ps2 = listaPaises[x+1]
    print(ps1[0],"-",ps2[0])
    if ps1[0] > ps2[0]:
      aux = listaPaises[x+1]
      listaPaises[x+1] = listaPaises[x]
      listaPaises[x] = aux

print("Lista paises ordenada:",listaPaises)