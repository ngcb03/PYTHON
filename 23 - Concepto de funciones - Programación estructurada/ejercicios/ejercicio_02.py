"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

Última modificación: 05-03-23

"""
# definimos funciones

def proceso():
  datos=cargar_datos()
  menor_dato(datos)
  print()

def cargar_datos():
  print("¡Obtener menor valor!")
  num1=float(input("Ingrese primer valor: "))
  num2=float(input("Ingrese segundo valor: "))
  num3=float(input("Ingrese tercer valor: "))
  datos=[]; datos.append(num1); datos.append(num2); datos.append(num3)
  return datos

def menor_dato(datos):
  menor=datos[0]
  for f in range(len(datos)-1):
    if menor>datos[f+1]:
      print(menor)
      menor=datos[f+1]
  print("Menor dato:",menor)

# llamamos funciones
proceso()
proceso()