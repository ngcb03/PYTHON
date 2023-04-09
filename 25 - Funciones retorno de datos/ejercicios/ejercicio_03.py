
"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.

Última modificación: 25-03-23

"""
# declaramos funciones
def retormnar_superficie(lado1,lado2):
  return (lado1*lado2)

def mayor(valor1,valor2):
  if valor1>valor2:
    return valor1
  else:
    return valor2


# instrucciones complementarias
print("¡Calcular superficie cuadrado!")
lado1 = float(input("Ingrese primer lado: "))
lado2 = float(input("Ingrese segundo lado: "))
print("Superficie cuadrado:",retormnar_superficie(lado1,lado2))
print("Mayor lado registrado:",mayor(lado1,lado2))
