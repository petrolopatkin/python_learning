# part 1 of logging module by the video of Corey Schafer
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.exception("You can't divide by zero")
    else:
        return result


num_1 = 5

num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')
sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')
mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')
div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')

# creating a file logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # creating a formatter
# formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# #creating a file handler
# file_handler = logging.FileHandler('employee.log')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)

# class Employee:
#     """A sample Employee class"""

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#         logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('John', 'Smith')
# emp_2 = Employee('Corey', 'Schafer')
# emp_3 = Employee('Jane', 'Doe')

# part 2 of logging module by the video of Corey Schafer