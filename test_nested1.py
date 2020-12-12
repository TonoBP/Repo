def bigger_price(lista) -> list:
    """
        TOP most expensive goods
    """
    def precio(lis):
        return lis['price']
    lista_ord = lista.sort(key=precio, reverse = True)
    print(lista)
    #print(lista_ord)

    return lista_ord

bigger_price([
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])
