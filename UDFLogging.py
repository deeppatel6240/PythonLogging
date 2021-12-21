import logging

from LogConfiguration import conf
from LogConfiguration.conf import CustomAdapter

logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {"id": None})

v = '123'
logger.info("hello", id=v)