"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.

Última modificación: 05-03-23

"""
# definimos funciones
def presentacion():
  print("¡Programa que suma de dos números!")
  separador()

def separador():
  print("**********************************")

def despedida():
  print("¡El programa a finalizado!")
  print("Hasta pronto...")

def carga_suma():
  num1=float(input("Ingrese primer valor: "))
  num2=float(input("Ingrese segundo valor: "))
  print("Suma resultante:",(num1+num2))

def proceso():
  presentacion()
  separador()
  carga_suma()
  separador()
  despedida()

# llamamos a funciones
proceso()