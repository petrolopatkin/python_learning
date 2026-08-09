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

    def is_food(self):
        if self.category == "Food":
            return True
        else:
            return False


    def change_price(self, new_price):
        self.price = new_price


item1 = Expense("09-08-2026", "Food", "Orange", 1.35)
item1.change_price(1.45)
item1.show()
print(item1.is_food())
item2 = Expense("09-08-2026", "Entertainment", "Cinema ticket", 10.45)
item2.show()
item3 = Expense("08-08-2026", "Shopping", "T-Shirt", 15)
item3.show()
expense1 = Expense("08-08-2026", "Food", "Chicken", 3.25)
print(expense1.is_food())