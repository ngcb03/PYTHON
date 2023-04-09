# Realizar la carga de valores enteros por teclado, almacenarlos en una 
# lista. Finalizar la carga de enteros al ingresar el cero. Mostrar 
# finalmente el tamaño de la lista.

# Progama: Cargar enteros en lista y mostrar cantidad de elementos
# Programador: Nicolas G. Camargo B.
# Última modificación: 29-01-23

listaEnteros = [] # Lista vacía para asignar valores enteros
sl = 1 # variable de salida

while sl != 0:
  listaEnteros.append(int(input("Ingrese valor entero: ")))
  if listaEnteros[(len(listaEnteros)-1)] == 0:
    sl=0

print("Cantidad elementos lista:",(len(listaEnteros)-1)) # El 0 no se cuenta en la lista!