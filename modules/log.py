import logging


def log(logger, level, filepath):
    logging.basicConfig(
        filemode="a",
        format="%(asctime)s %(levelname)s: %(funcName)s:%(lineno)d %(message)s",
        encoding="utf-8",
        datefmt="%d-%b-%y %H:%M:%S",
        filename=filepath,
    )
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s: %(funcName)s:%(lineno)d %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    handler = logging.FileHandler(filepath)
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
