from menu import products


def get_product_by_id(productId: int) -> dict:
    if not type(productId) == int:
        raise TypeError('product id must be an int')
    
    my_product = dict()
    for product in products:
        if product['_id'] == productId:
            my_product = product    
            
    return my_product

def get_products_by_type(productType: str) -> list:
    if not type(productType) == str:
        raise TypeError('product type must be a str')
    
    products_list = list()

    for product in products:
        if product['type'] == productType:
            products_list.append(product)
    
    return products_list


def add_product(menu: list, **item: dict) -> dict:
    item['_id'] = len(menu) + 1
    menu.append(item)

    return item


def menu_report():
    prices = list()
    for product in products:
        prices.append(product['price'])
    
    average_price = round(sum(prices) / len(prices), 2)

    types = list()
    for product in products:
        types.append(product['type'])
    
    type_dict = {
        'fruit': types.count('fruit'), 
        'vegetable': types.count('vegetable'), 
        'dairy': types.count('dairy'), 
        'drink': types.count('drink'), 
        'bakery': types.count('bakery')
    }
    type_list_sorted = sorted(type_dict.items(), key=lambda x:x[1])
    
    return f'Products Count: {len(products)} - Average Price: ${average_price} - Most Common Type: {type_list_sorted[-1][0]}'