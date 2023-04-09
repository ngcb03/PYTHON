"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su sup.

Última modificación: 13-03-23

"""
# declaramos funciones
def sup_cuadrado(lado):
  sup=lado*lado
  return sup

print("Obtener sup de un cuadrado!")
print("sup: ",sup_cuadrado(lado = float(input("Ingrese lado cuadrado: "))))
