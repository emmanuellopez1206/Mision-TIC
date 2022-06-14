# Datos solicitados por consola

CodigoProducto = int(input())
NombreProducto = str(input())
CantidadComprada = float(input())
ValorUnitario = float(input())

# Operaciones para calcular valor del producto sin aplicar IVA y el valor final del producto
ValorTotalSinIva = float(CantidadComprada * ValorUnitario)
ValorFinal = float(ValorTotalSinIva + (ValorTotalSinIva * 0.19))

# Impresiones solicitadas
print(CodigoProducto)
print(NombreProducto)
print(ValorTotalSinIva)
print(ValorFinal)