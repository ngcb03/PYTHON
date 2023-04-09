# Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por 
# pantalla el nombre de la persona con mayor altura.


# Programa: Altura mayor de dos personas
# Programador: Nicolas Camargo
# Última actualización: 12.01.23

print("Persona #1 ->")
nombrePer1 = input("Ingrese nombre: ")
edadPer1 = int(input("Ingrese edad: "))
alturaPer1 = float(input("Ingrese estatura Ej 1.75 ->  "))

print()

print("Persona #2 ->")
nombrePer2 = input("Ingrese nombre -> ")
edadPer2 = int(input("Ingrese edad -> "))
alturaPer2 = float(input("Ingrese estatura Ej 1.75 -> "))

if alturaPer1 != alturaPer2:
  if alturaPer1>alturaPer2:
    print("¡",nombrePer1,"tiene la que tiene mayor altura!")
  else:
    print("¡",nombrePer2,"tiene la que tiene mayor altura!")
else:
  print("¡Las dos personas tienen igual altura!")
