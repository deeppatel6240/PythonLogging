import logging

#logging.basicConfig(format='[%(process)d] [%(levelname)s]: %(message)s')
#logging.warning('This is a Warning')

logging.basicConfig(format='%(asctime)s [%(process)d] [%(levelname)s]: %(message)s', level=logging.INFO)
logging.info('Admin logged in into server this is first programmed by python logging fraamework')