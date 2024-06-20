# help developer to debug bug and find error by recording different intermediate events in a certain process
 
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

print()
import logging
logging.basicConfig(level=logging.DEBUG)
marks = 120
logging.error("Invalid marks:{} Marks must be between 0 to 100".format(marks))
subjects = ["Phy", "Maths"]
logging.warning("Number of subjects: {}. Should be at least three".format(len(subjects)))