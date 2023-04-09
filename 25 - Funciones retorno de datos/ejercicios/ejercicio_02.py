"""
Programador: Nicolas G. Camargo B.

Programa: Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

Última modificación: 20-03-23

"""
# declaramos funciones
def perimetro_cuadrado(lado):
  return (lado*4)


# instrucciones complementarias
print("¡Calcular perímetro de un cuadrado!")
print("Resultado:",perimetro_cuadrado(lado=float(input("Ingrese lado cuadrado: "))))