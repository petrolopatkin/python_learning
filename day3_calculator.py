#Simple Calculator
print('Calculator ')
number1 = int(input('First number: '))
number2 = int(input('Second number: '))
print('Sum: ' , number1 + number2)
#Area of the room
lenght = int(input('Lenght of the room: '))
height = int(input('Height of the room: '))
area = (lenght *  height)
print('Area of the room ' , area)
#Price Calculator
price = int(input('Enter a price: '))
tax = int(input('Enter a tax: '))
final_price = (price + (price * tax/100))
print('Final price ' , final_price)