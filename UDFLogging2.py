import logging


class CustomFilter(logging.Filter):
    COLOR = {
        "DEBUG": "GREEN",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "RED",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - [%(color)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %("
           "message)s",
)

logger = logging.getLogger(__name__)
logger.addFilter(CustomFilter())

logger.debug("debug message, color is green")
logger.info("info message, color is green")
logger.warning("warning message, color is yellow")
logger.error("error message, color is red")
logger.critical("critical message, color is red")
