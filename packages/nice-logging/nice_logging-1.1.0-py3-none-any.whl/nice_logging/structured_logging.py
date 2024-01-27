import logging

from .nice_logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, TRACE

class StructuredLogger:
	def __init__(self, parent_logger):
		self.parent_logger = parent_logger

	def critical(self, message, /, **kwargs):
		self.log(CRITICAL, message, **kwargs)

	def error(self, message, /, **kwargs):
		self.log(ERROR, message, **kwargs)

	def warning(self, message, /, **kwargs):
		self.log(WARNING, message, **kwargs)

	def info(self, message, /, **kwargs):
		self.log(INFO, message, **kwargs)

	def debug(self, message, /, **kwargs):
		self.log(DEBUG, message, **kwargs)

	def trace(self, message, /, **kwargs):
		self.log(TRACE, message, **kwargs)

	def log(self, level, message, stacklevel=1, /, **kwargs):
		self._log(level, message, kwargs, stacklevel=stacklevel+1)

	def _log(self, level, message, data, stacklevel=1):
		self.parent_logger._log(level, message, (), extra={ 'structured': True, 'structured_data': data }, stacklevel=stacklevel)
