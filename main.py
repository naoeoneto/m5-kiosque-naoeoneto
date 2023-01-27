from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report, add_product_extra
from menu import products
from management.tab_handler import calculate_tab

if __name__ == '__main__':
    print(get_product_by_id(32))

    print(get_products_by_type('vegetable'))

    new_product = {
            'title': 'Vegan Cupcake',
            'price': 10.0,
            'rating': 2,
            'description': 'Cupcake made with vegan products',
            'type': 'bakery',
        }
    print(add_product(products, **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    print(menu_report())

    required_keys = ("description", "price", "rating", "title", "type")
 
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    print(add_product_extra(products, *required_keys, **new_product))

    required_keys = ("description", "price", "rating", "title", "type")
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product_extra(products, *required_keys, **new_product))
