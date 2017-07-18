'''
Exceptions and handling.
'''

class TMError(Exception):
	''' Base class for exceptions in this module. '''
	pass
	
class PanOffsetError(TMError):
	''' 
	Exception raised for error s in the PanOffset class. 
	Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
	'''
	
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message
	