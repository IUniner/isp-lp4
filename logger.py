# import logging
# import logging.handlers
#
# logger = None
#
#
# def create_logger():
#     global logger
#     logger = logging.getLogger('Logger')
#     logger.setLevel(logging.DEBUG)
#     handler = logging.handlers.RotatingFileHandler("C:/Users/user/Desktop/info.log", maxBytes=1000000, backupCount=20)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)
#
#
# create_logger()
# logger.info("Text info")
# logger.debug("Text debug")
# logger.warning("Text warning")
# logger.error("Text error")
# logger.critical("Text critical")

import logging

# Define MESSAGE log level
MESSAGE = 25

# "Register" new loggin level
logging.addLevelName(MESSAGE, 'MESSAGE')  # addLevelName(25, 'MESSAGE')

# Verify
assert logging.getLevelName(MESSAGE) == 'MESSAGE'
message = 'This is a message'
logging.log(MESSAGE, message)

logging.Logger.message = message


class MyLogger(logging.Logger):
    def message(self, msg, *args, **kwargs):
        if self.isEnabledFor(MESSAGE):
            self._log(MESSAGE, msg, args, **kwargs)
        print(msg)


# or setattr(logging.Logger, 'message', message)



my_logger = MyLogger('Custom')

# my_logger.message('Here is a message')


logging.Logger.manager.loggerDict['Custom'] = my_logger

logger = logging.getLogger('Custom')
# logger.message('This is the same instance as my_logger')
assert logger is my_logger



# Use the new logger class
logger.warning('It works')
my_logger.message('Here is a message')
# logger.
# Log with custom log level:
# logger.log(MESSAGE, 'This is a message')
