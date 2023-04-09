# Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea 
# cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
# Mostrar la suma de los valores ingresados.

seguir="si"
suma=0

while seguir=="si":
    numEnt = int(input("Ingrese valor entero: "))
    suma+=numEnt
    seguir=''
    while seguir!='si' and seguir!='no':
      seguir = input("Desea cargar otro valor? (si / no): ")

print("Suma total:",suma)