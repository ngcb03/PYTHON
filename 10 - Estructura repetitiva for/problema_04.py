# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre 
# posteriormente la suma de los valores ingresados y su promedio. Este problema ya lo 
# desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez 
# valores por teclado.

sumaGen=0

for x in range(10):
  num = int(input("Ingrese valor -> "))
  sumaGen+=num

print("Suma general -> ",sumaGen)  
print("Promedio general -> ",(sumaGen/10))

# El resultado hubiese sido el mismo si llamamos a la funcion range con los valores: range(1,11)