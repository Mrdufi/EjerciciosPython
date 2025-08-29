nombre = input("Ingresa tu nombre: ")
ventas=float (input("precio original del producto: "))
descuento=float(input("porcentaje de descuento ejemplo 20 para 20%:"))


total= ventas-(ventas)*(descuento)/100
total=round(total,2)

print(f"Hola Adolfo, el precio final de tu producto con {descuento}% de descuento es {total}")