import itertools 

# itertools practice 
# task 1 chain()

warehouse_a = ["Laptop", "Mouse", "Keyboard"]
warehouse_b = ["Monitor", "Headphones", "Webcam"]

combined_task = itertools.chain(warehouse_a, warehouse_b)

for item in combined_task:
    print(item)

# task 2 islice()

logs = range(1_000_00)

result = itertools.islice(logs, 10)

print(list(result))

# task 3 groupby()
def get_orders(order):
    return order['customer']


orders = [
    {"customer": "Alice", "product": "Laptop", "price": 1200},
    {"customer": "Alice", "product": "Mouse", "price": 25},
    {"customer": "Bob", "product": "Monitor", "price": 350},
    {"customer": "Bob", "product": "Keyboard", "price": 80},
    {"customer": "Charlie", "product": "Headphones", "price": 150},
]

orders_group = itertools.groupby(orders, get_orders)

for customer, group in orders_group:
    total = 0
    for order in group:
        total += order['price']

    print(f"Customer: {customer}, Total: {total}")

# task 4 choose an instrument without any hints

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [1200, 25, 80, 350]

result_task4 = zip(products, prices)

for product, price in result_task4:
    print(f"Product: {product}, Price: {price}")