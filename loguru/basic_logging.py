#! /usr/bin/env python
# This is a basic logging example
# It will log the messages to the console

from loguru import logger

logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
logger.warning("Warning message")
logger.critical("Critical message")
logger.trace("Trace message")
logger.success("Success message")
