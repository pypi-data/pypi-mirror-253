from logging import StreamHandler, getLogger


def create_logger(name: str):
    logger = getLogger(name)
    stream_handler = StreamHandler()
    logger.addHandler(stream_handler)
    return logger
