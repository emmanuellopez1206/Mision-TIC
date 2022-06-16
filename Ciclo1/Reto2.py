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
    if TipoIVA == "1":
        ValorIVA = 0
    elif TipoIVA == "2":
        ValorIVA = ValorSinIVA * 0.05
    elif TipoIVA == "3":
        ValorIVA = ValorSinIVA * 0.19
    
    # Cálculos matemáticos solicitados
    ValorConIVA = ValorSinIVA + ValorIVA
    ValorTotalCompra += ValorConIVA
    ValorTotalIVA += ValorIVA

    # Impresiones solicitadas
    print(Codigo)
    print(NombreProducto)
    print(ValorSinIVA)
    print(ValorConIVA)

print(ValorTotalCompra)
print(ValorTotalIVA)

