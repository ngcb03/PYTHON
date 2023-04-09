"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

Última modificación: 17-03-23

"""
# declaramos funciones
def num_caracteres(nombre):
  return len(nombre)

# instrucciones complementarias
print("¡Número de caracteres de dos nombres!")
nombre1=input("Ingrese primer nombre: ")
print("Número caracteres:",num_caracteres(nombre1))
nombre2=input("Ingrese segundo nombre: ")
print("Número caracteres:",num_caracteres(nombre2))