"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.

Última modificación: 05-03-23

"""
# definimos las funciones
def carga_datos():
  datos=[]
  datos.append(int(input("Ingrese primer entero: ")))
  datos.append(int(input("Ingrese segundo entero: ")))
  datos.append(int(input("Ingrese tercer entero: ")))
  return datos

def mayor_dato(datos):
  mayor=datos[0]
  for k in range(len(datos)-1):
    if mayor<datos[k+1]:
      mayor=datos[k+1]
  print("Mayor dato:",mayor)

def separador():
  print("***********************")

# llamamos funciones
print("¡Obtener mayor de tres datos!")
separador()
datos=carga_datos()
separador()
mayor_dato(datos)
