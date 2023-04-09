"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)


Última modificación: 26-03-23

"""
# declaración de funciones
def multiplicar(lista,multiplicador):
    cont = 0
    while cont < len(lista):
        print(lista[cont],"x",multiplicador,"=",lista[cont]*multiplicador)
        print()
        cont+=1


# declaraciones complementarias
lista=[3,7,8,10,2]
print(lista)
print()
multiplicar(lista,3)