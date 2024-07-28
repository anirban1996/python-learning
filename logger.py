# import logging
# #there are 5 level of logging we can include or use 
# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')
#o/p: WARNING:root:this is a warning message
#ERROR:root:this is a error message
#CRITICAL:root:this is a critical message

#by default , only warning , critical and error will have a print statement so , if we need to print debug and info message as well then we need to change in basic setting of logging module.

# import logging
# logging.basicConfig(level=logging.DEBUG,)
# #there are 5 level of logging we can include or use 
# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')
'''
DEBUG:root:this is a debug message
INFO:root:this is a info message
WARNING:root:this is a warning message
ERROR:root:this is a error message
CRITICAL:root:this is a critical message
'''
#we can see that out logger by default called as root logger , so it is a best practice to use our own logger for better understanding , for that we can create our own logger module
#import helper#this will create a hierarchy og loggers. it starts at the root logger and all these new loggers get added to the hierarchy and they propagate upto the base logger ,

#log handler
#refer to helper.py




# import logging

# logging.basicConfig(level=logging.DEBUG, filename='log.log',filemode='w',format="%(asctime)s - %(levelname)s - %(message)s")

# # x=2

# # logging.debug(f"the value of x is {x}")

# try:
#     1/0
# except ZeroDivisionError as e :
#     #logging.error('dividing by zero',exc_info=True)#we have exception as well
#     logging.exception('ZeroDivisionError')


#creating custom logger

import logging

logging.basicConfig(level=logging.DEBUG, filename='log.log',filemode='w',format="%(asctime)s - %(levelname)s - %(message)s")

#custom logger object
logger=logging.getLogger(__name__)

#creating handler and formatter
handler=logging.FileHandler('test.log')
formatter=logging.Formatter("%(asctime)s - %(name)s- %(message)s")
#adding formatter
handler.setFormatter(formatter)
#adding handler
logger.addHandler(handler)

logger.info('this is a custom logger')