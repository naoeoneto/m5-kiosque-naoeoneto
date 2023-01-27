from menu import products


def get_product_by_id(productId: int):
    my_product = dict()

    for product in products:
        if product['_id'] == productId:
            my_product = product
    
    return my_product
            


def get_products_by_type(productType: str):
    products_list = list()

    for product in products:
        if product['type'] == productType:
            products_list.append(product)
    
    return products_list


def add_product(menu: list, **item: dict):
    item['_id'] = len(menu) + 1
    menu.append(item)

    return item