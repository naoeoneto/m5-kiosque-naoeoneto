from menu import products

def calculate_tab(orders: list):
    values = list()

    for product in products:
        for order in orders:
            if product['_id'] == order['_id']:
               value = product['price'] * order['amount']
               values.append(value)

    return {'subtotal': f'${round(sum(values), 2)}'}
