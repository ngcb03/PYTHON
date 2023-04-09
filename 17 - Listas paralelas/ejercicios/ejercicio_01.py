"""
Programador: Nicolas G. Camargo B.

Programa: Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

Última modificación: 01-02-23

"""
listaProductos = []
listaPrecios = []
cont = 0

print("¡Registro de productos!")
while cont<5:
  print("Producto #",cont+1)
  listaProductos.append(input("Ingrese producto: "))
  listaPrecios.append(float(input("Ingrese precio: ")))
  print()
  cont+=1

print()
print("Productos registrados: ")
for f in range(5):
  print(listaProductos[f],":",listaPrecios[f])

print()
print("Productos precio mayor al primero: ",listaProductos[0],"->",listaPrecios[0])
for f in range(2,5):
  if listaPrecios[f] > listaPrecios[0]:
    print(listaProductos[f],"->",listaPrecios[f])