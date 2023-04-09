"""
Programador: Nicolas G. Camargo B.


Programa: Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

Un ejemplo si se define por asignación:

padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
hijos=[["marcos","alberto","silvia"], [], ["oscar"]]
Como son listas paralelas podemos decir que la familia cuyos padres son "juan" y "ana" tiene tres hijos llamados "marcos", "alberto", "silvia". La segunda familia no tiene hijos y la tercera tiene solo uno.


Última modificación: 02-03-23

"""

padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
hijos=[["marcos","alberto","silvia"], [], ["oscar"]]

# listamos familias
for k in range(3):
  print("Familia #",k+1)
  print("Padres:",padres[k])
  print("Hijos:",hijos[0])
  print()

print("----------")
print()

# listamos al padre y cantidad de hijos que tiene
for k in range(3):
  print("Padre:",padres[k][0])
  print("Cantidad hijo:",len(hijos[k]))
  print()