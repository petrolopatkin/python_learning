import logging 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("app.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(handler)