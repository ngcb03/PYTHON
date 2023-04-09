"""
Programador: Nicolas G. Camargo B.

Programa: Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee. Luego imprimir el último elemento de la lista principal

Última modificación: 26-02-23

"""
# solicitamos componentes lista a crear
complistas=(-1)

print("¡Registrar componentes para lista!")
while complistas<=0:
  complistas=int(input("Ingrese cantidad: "))

lista=[[]]*complistas

for k in range(len(lista)):
  for x in range(2):
    lista[k].append(0)
    lista[k].append(1)
    break;
  break;


print("Componentes lista:",lista)
print("Última componente lista:",lista[len(lista)-1])