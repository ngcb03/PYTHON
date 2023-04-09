"""
Programador: Nicolas G. Camargo B.

Programa: Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

Última modificación: 26-03-23

"""
# declaramos funciones
def suma_elementos_lista(lista):
  sumaTotal=0
  for f in lista:
    sumaTotal+=f
  return sumaTotal

def mayor_valor_lista(lista):
  mayorLista=lista[0]
  for f in lista:
    if f>mayorLista:
      mayorLista=f
  return mayorLista

def menor_valor_lisa(lista):
  menorLista=lista[0]
  for f in lista:
    if f<menorLista:
      menorLista=f
  return menorLista


# instrucciones complementarias
lista=[]
seguir = True

print("¡Operaciones en listas!")
while(seguir):
  lista.append(float(input("Ingrese valor: ")))
  aux = int(input("Desea resitrar otro elemento? 0/no - 1/si: "))
  if aux==0:
    seguir=False

print("Suma elementos lista:",suma_elementos_lista(lista))
print("Mayor elemento lista:",mayor_valor_lista(lista))
print("Menor elemento lista:",menor_valor_lisa(lista))