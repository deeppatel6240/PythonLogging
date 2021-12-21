import logging

from LogConfiguration import conf
from LogConfiguration.conf import CustomAdapter

logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {"id": None})

logger.info("hello", id='123')