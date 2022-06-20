CantidadProductos = int(input())
Cont = 0

#Variables acumuladoras
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


FinalList = [ListCode, ListName, ListTaxValue, ListProductValue, ListFinalValue]

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

    #Calcular el tipo de IVA para cada producto.
    if TipoIVA == "1":
        TotalIVA = 0
        ListTaxValue.append(TotalIVA)
    elif TipoIVA == "2":
        TotalIVA = ValorSinIVA * 0.05
        ListTaxValue.append(TotalIVA)
    elif TipoIVA == "3":
        TotalIVA = ValorSinIVA * 0.19
        ListTaxValue.append(TotalIVA)

    # Cálculos solicitados y añadidos a sus respectivas listas.
    ValorConIVA = ValorSinIVA + TotalIVA
    ListFinalValue.append(ValorConIVA)
    ValorTotalCompra += ValorConIVA
    ValorTotalIVA += TotalIVA

# Porción de código usado para acomodar la FinalList a través de diccionarios.
FinalList2 = FinalList.copy()
elements = FinalList2[1]
FinalList2.pop(1)
dic = {}
for i in range(len(elements)):
    lista = []
    for j in FinalList2:
        lista.append(j[i])
    dic[elements[i]] = lista
    #List comprehension (La línea 65 reemplza las lineas 60 a la 63)
    #dic[elements[i]] = [ j[i] for j in FinalList2]
sorted_dict = {k:v for k,v in sorted(dic.items())}
for i in sorted_dict.values():

    for j in i:
        print(j)

# Últimas impresiones solicitadas
print(ValorTotalCompra)
print(ValorTotalIVA)