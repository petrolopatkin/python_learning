products = {
    "Banana": 10,
    "Milk": 15,
    "Beer": 5,
    "Chicken": 20,
    "Beef": 15,
    "Juice": 6,
    "Ice Cream": 4
}
def show_products():
    for item in products:
        print(item, products[item])


show_products()