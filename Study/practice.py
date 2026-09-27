# This is my python practice in order to not forget python syntax while writing in JavaScript
# Task 1(Simple function)
def calculate_price(price, quantity):
    return price * quantity


result = calculate_price(25, 10)
print(result)

# Task 2 simple function + if/else statement
def check_score(score):
    if score == 0:
        return "Invalid score"
    elif score < 50:
        return "Fail"
    elif score > 50 and score <= 69:
        return "Pass"
    elif score > 69 and score <= 89:
        return "Great"
    elif score > 89 and score <= 100:
        return "Excellent"
    else:
        return "You didn't attend the test"


print(check_score(45))
print(check_score(75))
print(check_score(95))

# Task 3 list + fictionaries + loop
users = [
    {
        "name": "Peter",
        "age": 18,
        "student": True
    },
    {
        "name": "Anna",
        "age": 19,
        "student": True
    },
    {
        "name": "John",
        "age": 22,
        "student": False
    },
    {
        "name": "Mark",
        "age": 17,
        "student": False
    }
]

for user in users:
    if user["age"] >= 18 and user["student"] == True:
        print(user["name"])
    else:
        print(f"{user['name']} doesn't match conditions")