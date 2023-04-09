# Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio
# del producto)

precio = int(input("Ingresa precio del producto: "))
cantidad = int(input("Ingresa cantidad de productos a llevar: "))
importe = precio * cantidad
print("El importe a pagar es",importe)
