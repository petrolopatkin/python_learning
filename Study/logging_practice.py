# a little practice with logging module
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def create_user(username, age):
    if not username:
        logger.warning('A user has to have a username')
    elif age < 0:
        logger.error("Age cannot be less than zero")
        raise ValueError("Age cannot be less than zero")
    else:
        logger.info(f"Username: {username}, Age: {age}")


create_user("Peter", 18)
create_user("", 25)
create_user("Anna", -5)