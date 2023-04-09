"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

Última modificación: 05-03-23

"""
# definimos función de carga_suma y seperador
def carga_suma():
  num1=float(input("Ingrese primer valor: "))
  num2=float(input("Ingrese segundo valor: "))
  print("Suma resultante:",num1+num2)

def separador():
  print("*******************************") 


# cargamos y listamos los valores
for x in range(5):
  carga_suma()
  separador()