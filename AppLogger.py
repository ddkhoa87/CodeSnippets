'''
Logger functions.
'''

import logging

def initLogger(logFileName):
	
	try:
		# Clear the current log file
		with open(logFileName, 'w'):
			pass
		
		logger = logging.getLogger(logFileName)
		logger.setLevel(logging.DEBUG)
		
		fileHandler = logging.FileHandler(logFileName)
		fileHandler.setLevel(logging.DEBUG)
		
		logger.addHandler(fileHandler)
		logger.debug('Init Logger Successfully.')
				
		return logger
	
	except:
		return None

def cleanUpLogger(logger):
	
	if logger is None:
		return
	
	logger.info('Cleaned up successfully.')
	
	handlers = logger.handlers[:]
	for hdl in handlers:
			hdl.close()
			logger.removeHandler(hdl)