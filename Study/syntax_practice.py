# syntax practice in order to not forget python language
# task 1
products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Keyboard", "price": 80, "stock": 12},
    {"name": "Monitor", "price": 350, "stock": 3},
    {"name": "Headphones", "price": 150, "stock": 0}
]


def get_available_products(products):
    result = []

    for product in products:
        if product["stock"] > 0 and product["price"] < 500:
            result.append({
                "name": product['name'],
                "price": product['price']
            })
    return result


def calculate_invertory_value(products):
    total = 0
    for product in products:
        total += product['price'] * product['stock']
    return total


def get_stock_report(products):
    report = {}
    for product in products:
        if product['stock'] > 0:
            report[product['name']] = product['price'] * product['stock']
    return report

print(get_available_products(products))
print(calculate_invertory_value(products))
print(get_stock_report(products))

# task 2
orders = [
    {"customer": "Alice", "product": "Laptop", "price": 1200, "quantity": 2},
    {"customer": "Bob", "product": "Mouse", "price": 25, "quantity": 3},
    {"customer": "Alice", "product": "Keyboard", "price": 80, "quantity": 1},
    {"customer": "Charlie", "product": "Monitor", "price": 350, "quantity": 2},
    {"customer": "Bob", "product": "Headphones", "price": 150, "quantity": 1}
]


def calculate_customer_spending(orders):
    customer_spending = {}
    for order in orders:
        if order['customer'] not in customer_spending:
            customer_spending[order['customer']] = 0

        customer_spending[order['customer']] += order['price'] * order['quantity']
    return customer_spending

print(calculate_customer_spending(orders))