import logging, os
from logging import DEBUG, WARNING, CRITICAL, INFO, NOTSET



def get_logger(logfile=None, logger_name=None,  mode='a', loglevel=DEBUG):

    logger = logging.getLogger(logger_name or __name__)

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    if logfile:
        diranme = os.path.dirname(logfile)
        os.makedirs(diranme, exist_ok=True)
        fileHandler = logging.FileHandler(logfile,mode=mode)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    logger.setLevel(level=loglevel)
    return logger

