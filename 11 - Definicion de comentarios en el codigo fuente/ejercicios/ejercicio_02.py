# Confeccionar un programa que solicite la carga de 10 valores reales por teclado.
# Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre
# del programa, el programador y la fecha de la última modificación. Utilizar el 
# caracter para los comentarios.

# Programa: Suma 10 números reales ingresados
# Programador: Nicolas G. Camargo B.
# Última modificación: 09-01-23

sumaR=0

for f in range(10):
  # La función float convierte a reales
  num = float(input("Ingrese valor de tipo real -> "))
  sumaR+=num

print("Suma general:",sumaR)
