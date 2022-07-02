CantidadProductos = int(input())
Cont = 0
ValorTotalCompra = 0
ValorTotalIVA= 0

# Listas donde se almacena la información solicitada
ListCode = []
ListName = []
ListLot = []
ListUnitValue = []
ListTax = []
ListProductValue = []
ListTaxValue = []
ListFinalValue = []

while Cont < CantidadProductos:
    Cont += 1
    # Datos solicitados por consola y añadidos a las listas
    Codigo = int(input())
    ListCode.append(Codigo)
    NombreProducto = input()
    ListName.append(NombreProducto)
    CantidadComprada = float(input())
    ListLot.append(CantidadComprada)
    ValorUnitario = float(input())
    ListUnitValue.append(ValorUnitario)
    ValorSinIVA = CantidadComprada * ValorUnitario
    ListProductValue.append(ValorSinIVA)
    TipoIVA = input()
    ListTax.append(TipoIVA)

    #Calcular el tipo de IVA para cada producto y añadirlo a su respectiva lista.
    ValorIVA = 0
    if TipoIVA == "1":
        TotalIVA = 0
    elif TipoIVA == "2":
        TotalIVA = ValorSinIVA * 0.05
    elif TipoIVA == "3":
        TotalIVA = ValorSinIVA * 0.19
    ListTaxValue.append(TotalIVA)

    # Cálculos solicitados y añadidos a sus respectivas listas.
    ValorConIVA = ValorSinIVA + TotalIVA
    ListFinalValue.append(ValorConIVA)
    ValorTotalCompra += ValorConIVA
    ValorTotalIVA += TotalIVA

# Impresiones de longitud solicitadas.
print(len(ListCode))
print(len(ListName))
print(len(ListLot))
print(len(ListUnitValue))
print(len(ListTax))

# impresión de los productos según orden solicitado.
for i in range(CantidadProductos):
    print(ListCode[i])
    print(ListName[i])
    print(ListProductValue[i])
    print(ListFinalValue[i])

# Últimas impresiones solicitadas
print(ValorTotalCompra)
print(ValorTotalIVA)
