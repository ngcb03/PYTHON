"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

Última modificación: 05-03-23

"""
# definimos las funciones
def cargar_dato():
  print("¡Obtener perímetro o superficie de un cuadrado!")
  dato=float(input("Ingrese lado cuadrado: "))
  separador()
  operaciones(dato)

def operaciones(dato):
  print("Operaciones disponibles:")
  print("1 para hallar perímetro")
  print("2 para halla superficie")
  eleccion=int(input("Elegir: "))
  separador()
  
  if eleccion==1:
    obtener_perimetro(dato)
  else:
    obtener_superficie(dato)

def obtener_perimetro(lado):
  print("Perímetro resultante:",(lado)*4)
def obtener_superficie(lado):
  print("Suerficie resultante:",(lado*lado))

def separador():
  print("*************************")


# llamamos funciones
cargar_dato()
separador()
print("Hasta pronto...")