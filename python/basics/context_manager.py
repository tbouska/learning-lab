from contextlib import contextmanager
import logging

@contextmanager 
def debug_logging(level): 
    logger = logging.getLogger() 
    old_level = logger.getEffectiveLevel() 
    logger.setLevel(level) 
    try: 
        yield 
    finally: 
        logger.setLevel(old_level)

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
with debug_logging(logging.DEBUG):
    logging.warning("I warn you")
    logging.debug("This wouldn't normally show")
