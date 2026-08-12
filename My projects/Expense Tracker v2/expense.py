class Expense:
    def __init__(self, date, category, item, price ):
        self.date = date
        self.category = category
        self.item = item
        self.price = price


    def show(self):
        print(f"""
Date: {self.date}
Category: {self.category}
Item: {self.item}
Price: {self.price}""")


    def change_price(self, new_price):
        self.price = new_price


