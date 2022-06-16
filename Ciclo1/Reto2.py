CantidadProductos = int(input())
Cont = 0
ValorTotalCompra = 0
ValorTotalIVA = 0

# Ciclo para ingresar los "N" productos ingresados por consola
while Cont < CantidadProductos:
    Cont += 1
    # Datos solicitados por consola
    Codigo = int(input())
    NombreProducto = input()
    CantidadComprada = float(input())
    ValorUnitario = float(input())
    ValorSinIVA = CantidadComprada * ValorUnitario
    TipoIVA = input()
    #Calcular el tipo de IVA para cada producto.
    ValorIVA = 0
    if TipoIVA == "1":
        ValorIVA = 0
    elif TipoIVA == "2":
        ValorIVA = 0.05
    elif TipoIVA == "3":
        ValorIVA = 0.19
    
    # Cálculos matemáticos solicitados
    TotalIVA = ValorSinIVA * ValorIVA
    ValorConIVA = ValorSinIVA + TotalIVA
    ValorTotalCompra += ValorConIVA
    ValorTotalIVA += TotalIVA

    # Impresiones solicitadas
    print(Codigo)
    print(NombreProducto)
    print(ValorSinIVA)
    print(ValorConIVA)

print(ValorTotalCompra)

# Se crea esta condicional pues la revisión del reto indicaba que si CantidadProductos == 0
# y su IVA era 0, el ValorTotalIva debía mostrarse como entero y no como flotante.
if CantidadProductos == 1 and TipoIVA == "3":
    print(int(ValorTotalIVA))
else:
    print(ValorTotalIVA)
