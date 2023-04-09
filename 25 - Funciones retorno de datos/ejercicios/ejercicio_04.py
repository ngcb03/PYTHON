"""
Programador: Nicolas G. Camargo B.

Programa: Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A

Última modificación: 20-03-23

"""
# declaramos funciones

def cantidad_letras_aA(oracion):
  cant_letras_aA = 0
  for f in oracion:
    if f=='a' or f=='A':
      cant_letras_aA+=1
  return cant_letras_aA


# instrucciones complementarias
print("¡Cantidad de letras 'a' y 'A' de una oración!")
oracion = input("Ingrese un oración: ")
print("Resultado:",cantidad_letras_aA(oracion))