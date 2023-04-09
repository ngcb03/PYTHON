"""
Programador: Nicolas G. Camargo B.

Programa: Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.

Última modificación: 26-03-23

"""
# declaramos funciones
def mayorMenorLista(lista_enteros):
  mayor = lista_enteros[0]
  menor = lista_enteros[0]
  for f in lista_enteros:
    if f>mayor:
      mayor=f
    else:
      if f<menor:
        menor=f
  lista_aux = [menor,mayor]
  return lista_aux


# bloque principal
lista_enteros = []
lim = 0

print("¡Registro de 5 enteros!")
while lim<5:
  lista_enteros.append(int(input("Ingrese valor entero: ")))
  lim+=1

lista_resultante = mayorMenorLista(lista_enteros)
print("Menor lista:",lista_resultante[0])
print("Mayor lista:",lista_resultante[1])