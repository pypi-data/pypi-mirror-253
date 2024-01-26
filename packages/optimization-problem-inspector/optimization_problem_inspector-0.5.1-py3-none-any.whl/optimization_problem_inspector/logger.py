import logging
import sys

from loguru import logger

from .config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

# change loguru level logging
# ref: https://github.com/Delgan/loguru/issues/51
logger.remove()
logger.add(sys.stderr, level=LOG_LEVEL)
