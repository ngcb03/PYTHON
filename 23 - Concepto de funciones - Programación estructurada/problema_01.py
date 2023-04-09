"""
Programador: Nicolas G. Camargo B.

Programa: Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones.

Última modificación: 05-03-23

"""
# definimos la función presentación
def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")

# definimos función de cargar_suma que reciba dos argumentos
def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)

# definimos la función de finalización
def finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")


# llamamos función presentación 
presentacion()

# solicitamos datos
carga_suma()

# llamamos función finalización
finalizacion()