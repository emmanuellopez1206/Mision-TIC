CantidadProductos = int(input())
Cont = 0
ValorTotalCompra = 0
ValorTotalIVA= 0

# Diccionarios con el nombre del artículo y sus respectivos precios. La llave de ambos diccionarios corresponde al código del producto.
articulos = {1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios = {1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

# Listas donde se almacena la información solicitada
ListCode = []
ListLot = []
ListTax = []
ListProductValue = []
ListTaxValue = []
ListFinalValue = []

while Cont < CantidadProductos:
    Cont += 1
    # Datos solicitados por consola y añadidos a las listas
    Codigo = int(input())
    ListCode.append(Codigo)
    CantidadComprada = float(input())
    ListLot.append(CantidadComprada)
    ValorSinIVA = CantidadComprada * precios[Codigo]
    ListProductValue.append(ValorSinIVA)
    TipoIVA = input()
    ListTax.append(TipoIVA)

    #Calcular el tipo de IVA para cada producto y añadirlo a su respectiva lista.
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

# Creamos la función con el método burbuja para ordenar las listas en orden alfabético
def Ordenar(Lista:list)->None:
    Temporal = Lista[i]
    Lista[i] = Lista[i+1]
    Lista[i+1] = Temporal

# Ordenamiento de las listas usando la función creada anteriormente.
for k in range(len(ListCode)-1):
    for i in range(len(ListCode)-1):
        if ListCode[i] > ListCode[i+1]:
            Ordenar(ListCode)         
            Ordenar(ListProductValue)
            Ordenar(ListFinalValue)

# impresión de los productos según orden solicitado.
for i in range(CantidadProductos):
    print(ListCode[i])
    print(articulos[ListCode[i]])
    print(ListProductValue[i])
    print(ListFinalValue[i])

# Últimas impresiones solicitadas
print(ValorTotalCompra)
print(ValorTotalIVA)