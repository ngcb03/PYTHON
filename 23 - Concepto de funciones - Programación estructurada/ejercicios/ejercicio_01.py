"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

Última modificación: 05-03-23

"""
# definimos funciones
def obtener_cuadrado():
  print("¡Obtener cuadrado de un entero!")
  ent=int(input("Ingrese valor entero: "))
  print("Cuadrado de",ent,":",ent*ent)

def carga_producto():
  print("¡Obtener producto de dos valores!")
  num1=float(input("Ingrese primer valor: "))
  num2=float(input("Ingrese segundo valor: "))
  print("Producto resultante:",(num1*num2))

# llamamos la funciones
obtener_cuadrado()
print()
carga_producto()