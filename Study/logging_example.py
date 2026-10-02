import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     return a / b


# num_1 = 5

# num_2 = 10

# add_result = add(num_1, num_2)
# logging.debug(f'Add: {num_1} + {num_2} = {add_result}')
# sub_result = subtract(num_1, num_2)
# logging.debug(f'Sub: {num_1} - {num_2} = {sub_result}')
# mul_result = multiply(num_1, num_2)
# logging.debug(f'Mul: {num_1} * {num_2} = {mul_result}')
# div_result = divide(num_1, num_2)
# logging.debug(f'Div: {num_1} / {num_2} = {div_result}')

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')