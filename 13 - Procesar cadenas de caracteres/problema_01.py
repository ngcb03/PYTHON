# Ya hemos visto que podemos cargar una cadena de caracteres por asignación:

#con doble comillas
cadena1="juan"
#el resultado es igual con simple comillas
cadena2='ana'

# También podemos cargarla por teclado:
nombre=input("Ingrese su nombre:")

""" 
Podemos utilizar los operadores relacionales para identificar si dos cadenas son iguales, distintas o cual es la mayor alfabética:

== Igualdad
!= Desigualdad
< menor
<= menor o igual
> mayor
>= mayor o igual

"""

# Como su nombre lo indica una cadena de caracteres está formada generalmente por varios 
# caracteres (de todos modos podría tener solo un caracter o ser una cadena vacía)
# Podemos acceder en forma individual a cada caracter del string mediante un subíndice:

nombre='nicolas'
print(nombre[0])   #se imprime una j
if nombre[0]=="n": #verificamos si el primer caracter del string es una j
    print(nombre)
    print("comienza con la letra n")

# Los subíndices comienzan a numerarse a partir del cero.
# Si queremos conocer la longitud de un string en Python disponemos de una función llamada len 
# que retorna la cantidad de caracteres que contiene:

nombre='nicolas'
print("Cantidad de caracteres del nombre nicolas:",len(nombre))

# El programa anterior imprime un 4 ya que la cadena nombre almacena 'juan' que tiene cuatro 
# caracteres.