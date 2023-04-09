# Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente 
# o si son iguales.

# Programa: Nombre más largo
# Programador: Nicolas Camargo
# Última actualización: 14-01-23



# Cuando trabajamos con cadenas de caracteres al utilizar el operador > estamos verificando si 
# una cadena es mayor alfabéticamente a otra (esto es distinto a cuando trabajamos con enteros o 
# flotantes)

# Por ejemplo 'luis' es mayor a 'carlos' porque la 'l' se encuentra más adelante en el 
# abecedario que la 'c'.



print("Persona #1")
nombre1 = input("Ingrese su nombre -> ")

print("Persona #2")
nombre2 = input("Ingrese su nombre -> ")

if nombre1!=nombre2:
  if nombre1>nombre2:
    print("¡La persona",nombre1,"tiene un nombre alfabéticamente mayor!")
  else:
    print("¡La persona",nombre2,"tiene un nombre alfabéticamente mayor!")
else:
  print("¡Los nombres son igual de mayores alfabéticamente!")