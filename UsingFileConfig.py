import logging
import logging.config

fname = 'Log Configuration/file.conf'

logging.config.fileConfig(fname=fname, disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')