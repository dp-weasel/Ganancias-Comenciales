# -*- encoding: utf-8 -*-

def Calculo(cantidad, precio):
	total = 0
	for x in range(0, len(cantidad)):
		total = total + (cantidad[x] * precio[x])
	return total

def Porcentaje(precio_compra, precio_venta):
	valor = ((precio_venta-precio_compra)*100)/precio_compra
	return valor

productos = []
cantidad = []
precio_compra = []
precio_venta = []

print '*************** Ingreso de Datos ***************'
opcion = 's'
while opcion != 'n':
	valor = raw_input("Nombre del producto: ")
	productos.append(valor)

	valor = input("Cantidad del producto: ")
	cantidad.append(valor)

	valor = input("Precio unitario del producto: ")
	precio_compra.append(valor)

	valor = input("Precio de venta del producto: ")
	precio_venta.append(valor)

	opcion = raw_input("¿Desea ingresar otro producto? (S/n): ")

inversion = Calculo(cantidad, precio_compra)
ganancia_total = int(Calculo(cantidad, precio_venta))
ganancia_neta = int(ganancia_total - inversion)


print '*************** Resultados del Negocio ***************'

for x in range(0, len(productos)):
	print '1)',productos[x]+':',Porcentaje(precio_compra[x], precio_venta[x]), '% de ganancia'

print 'Ganancia Total: ',ganancia_total
print 'Ganancia Netal: ',ganancia_neta

