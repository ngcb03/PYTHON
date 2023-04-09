# Realizar un programa que solicite la carga por teclado de dos números,
# si el primero es mayor al segundo informar su suma y diferencia, en caso
# contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))

if num1>num2:
    suma=num1+num2
    print("La suma entre num1 y num2 es",suma)
    diferencia=num1-num2
    print("La diferencia entre num1 y num2 es",diferencia)
else:
    producto=num1*num2
    print("El producto entre num1 y num2 es",producto)
    division=num1/num2
    print("La división entre num1 y num2 es",division)
