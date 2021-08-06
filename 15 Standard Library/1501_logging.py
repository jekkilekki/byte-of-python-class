# 1501_logging.py

import os, platform, logging

if platform.platform().startswith('Windows'):
         log_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
         log_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Logging to', log_file)

logging.basicConfig(
         level    = logging.DEBUG,
         format   = '%(asctime)s : %(levelname)s : %(message)s',
         filename = log_file,
         filemode = 'w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
