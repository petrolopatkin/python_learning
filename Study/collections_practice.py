from collections import Counter
from collections import defaultdict

# Counter practice
# task 1
actions = [
    "login",
    "view_product",
    "login",
    "purchase",
    "view_product",
    "login",
    "logout",
    "purchase",
    "view_product",
    "login",
    "purchase"
]

def count_actions(actions):
    my_count = Counter(actions)
    return my_count


print(count_actions(actions))

# task 2 return 3 most poplar products as well as their count
purchases = [
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse",
    "Laptop",
    "Monitor",
    "Mouse",
    "Keyboard",
    "Laptop"
]


def get_popular_products(purchases):
    my_count = Counter(purchases)
    return my_count.most_common(3)


print(get_popular_products(purchases))

# task 3 show all http-log answers but only those who have code >= 400
status_codes = [
    200, 200, 404, 500, 200,
    404, 201, 200, 500, 404,
    200, 403, 404
]


def analyze_status_codes(status_codes):
        errors = []
        for code in status_codes:
             if code >= 400:
                errors.append(code)
        return Counter(errors)


print(analyze_status_codes(status_codes))

# defaultdict practice
# task 1
orders = [
    {"customer": "Alice", "product": "Laptop"},
    {"customer": "Bob", "product": "Mouse"},
    {"customer": "Alice", "product": "Keyboard"},
    {"customer": "Charlie", "product": "Monitor"},
    {"customer": "Bob", "product": "Headphones"},
    {"customer": "Alice", "product": "Mouse"}
]


def group_orders_by_customer(orders):
     orders_by_customer = defaultdict(list)
     for order in orders:
          orders_by_customer[order['customer']].append(order['product'])
     return orders_by_customer


print(group_orders_by_customer(orders))

# task 2
orders = [
    {"customer": "Alice", "product": "Laptop", "price": 1200},
    {"customer": "Bob", "product": "Mouse", "price": 25},
    {"customer": "Alice", "product": "Keyboard", "price": 80},
    {"customer": "Charlie", "product": "Monitor", "price": 350},
    {"customer": "Bob", "product": "Headphones", "price": 150},
    {"customer": "Alice", "product": "Mouse", "price": 25}
]


def customer_spending(orders):
     spent_by_customer = defaultdict(int)

     for order in orders:
          spent_by_customer[order['customer']] += order['price']
     return spent_by_customer


print(customer_spending(orders))