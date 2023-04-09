"""
Programador: Nicolas G. Camargo B.

Programa: Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

Última modificación: 18-02-23

"""
paises=['Colombia','Jamaica','Panamá','Mexico','Bolivia']
habitantes=[51520000,2828000,4351000,126700000,12080000]

ps_orden=paises
hab_desorden=habitantes

ps_desorden=paises
hab_orden=habitantes

for f in range(4):
   for x in range(4):
     ps1=paises[x]
     ps2=paises[x+1]
     
     if ps1[0]>ps2[0]:
       aux=paises[x]
       ps_orden[x]=paises[x+1]
       ps_orden[x+1]=aux
       
       aux=habitantes[x]
       hab_desorden[x]=habitantes[x+1]
       hab_desorden[x+1]=aux
       
     if habitantes[x]<habitantes[x+1]:
       aux=habitantes[x]
       hab_orden[x]=habitantes[x+1]
       hab_orden[x+1]=aux
        
       aux=paises[x]
       ps_desorden[x]=paises[x+1]
       ps_desorden[x+1]=aux

print("Paises orden alfabétio: ")
print(ps_orden)
print(hab_desorden)
print()
print("Habitantes orden mayor-menor cantidad:")
print(hab_orden)
print(ps_desorden)