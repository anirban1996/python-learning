# import logging

# logger=logging.getLogger(__name__)
# #If I do not want to propagate to the base logger then we can sue the below setting
# logger.propagate=False
# logger.info('this is from helper')

import logging
logger=logging.getLogger(__name__)
#create handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler('File.log')

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s-%(message)s-%(levelname)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#add handlers

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')