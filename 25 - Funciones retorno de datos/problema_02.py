"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

Última modificación: 17-03-23

"""
# declaramos funciones
def entero_mayor(ent1,ent2):
  if ent1>ent2:
    return ent1
  return ent2

# instrucciones complementarias
print("Valor mayor entre 43234 y 53423:")
print(entero_mayor(43234,53423))