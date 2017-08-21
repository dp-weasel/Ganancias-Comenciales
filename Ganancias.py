# -*- encoding: utf-8 -*-

def Calculo(cantidad: int, precio: float):
  total = 0
  for x in range(0, len(cantidad)):
    total = total + (cantidad[x] * precio[x])
  return total

def Porcentaje(precio_compra: float, precio_venta: float):
  valor = ((precio_venta-precio_compra)*100)/precio_compra
  return valor

productos = []
cantidad = []
precio_compra = []
precio_venta = []

print ('*************** Ingreso de Datos ***************')
opcion = 's'
while opcion != 'n':
  valor = input("Nombre del producto: ")
  productos.append(valor)

  valor = int(input("Cantidad del producto: "))
  cantidad.append(valor)

  valor = float(input("Precio unitario del producto: "))
  precio_compra.append(valor)

  valor = float(input("Precio de venta del producto: "))
  precio_venta.append(valor)

  opcion = input("¿Desea ingresar otro producto? (S/n): ")

inversion = Calculo(cantidad, precio_compra)
ganancia_total = int(Calculo(cantidad, precio_venta))
ganancia_neta = int(ganancia_total - inversion)


print ('*************** Resultados del Negocio ***************')

for x in range(0, len(productos)):
  print ('1)',productos[x]+':',Porcentaje(precio_compra[x], precio_venta[x]), '% de ganancia')

print ('Ganancia Total: ',ganancia_total)
print ('Ganancia Netal: ',ganancia_neta)

