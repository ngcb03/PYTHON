# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

oracionTeclado = input("Ingrese oración: ")
cont = 0 # contador
esp = 0 # cantidad de espacios

while cont < len(oracionTeclado):
  if oracionTeclado[cont]==' ':
    esp+=1
  cont+=1

print("Cantidad de espacios en la oración:",esp)