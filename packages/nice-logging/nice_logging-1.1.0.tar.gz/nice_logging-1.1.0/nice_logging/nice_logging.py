import functools
import logging

CRITICAL = logging.CRITICAL
ERROR    = logging.ERROR
WARNING  = logging.WARNING
INFO     = logging.INFO
DEBUG    = logging.DEBUG
TRACE    = 1

DEFAULT_FORMAT = "%(asctime)s [%(level_label)s] [%(name)s] %(message)s"
DEFAULT_STYLED_FORMAT = "%(style_begin)s" + DEFAULT_FORMAT + "%(style_end)s"
DEFAULT_STYLES = {
	CRITICAL: { 'level_label': "CRIT ", 'style_begin': "\033[95m", 'style_end': "\033[0m" },
	ERROR:    { 'level_label': "ERROR", 'style_begin': "\033[91m", 'style_end': "\033[0m" },
	WARNING:  { 'level_label': "WARN ", 'style_begin': "\033[93m", 'style_end': "\033[0m" },
	INFO:     { 'level_label': "INFO ", 'style_begin': "\033[97m", 'style_end': "\033[0m" },
	DEBUG:    { 'level_label': "DEBUG", 'style_begin': "\033[37m", 'style_end': "\033[0m" },
	TRACE:    { 'level_label': "TRACE", 'style_begin': "\033[90m", 'style_end': "\033[0m" },
}

def trace(logger, msg, *args, **kwargs):
	"""
	Log formatted message with severity 'TRACE'.
	"""
	logger.log(TRACE, msg, *args, **kwargs)

def getLogger(name=None):
	logger = logging.getLogger(name)
	logger.trace = functools.wraps(trace)(lambda msg, *args, **kwargs: trace(logger, msg, *args, **kwargs))
	return logger

def getStructuredLogger(name=None):
	from . import structured_logging
	logger = getLogger(name)
	return structured_logging.StructuredLogger(logger)

def basicConfig(**kwargs):
	logging.basicConfig(**kwargs)
	root_logger = logging.getLogger()

	for handler in root_logger.handlers:
		if isinstance(handler, logging.StreamHandler):
			def_fmt = DEFAULT_STYLED_FORMAT
		else:
			def_fmt = DEFAULT_FORMAT

		fmt = kwargs.pop('format', def_fmt)
		datefmt = kwargs.pop('datefmt', None)
		style = kwargs.pop('style', '%')
		handler.formatter = NiceFormatter(fmt=fmt, datefmt=datefmt, style=style)

class NiceFormatter(logging.Formatter):
	def format(self, record):
		if getattr(record, 'structured', False):
			message = record.msg
			data = getattr(record, 'structured_data', {})
			record.msg = "%s %r"
			record.args = (message, data)

		level = max(filter(lambda lvl: record.levelno >= lvl, DEFAULT_STYLES.keys()))
		record.level_label = DEFAULT_STYLES[level]['level_label']
		record.style_begin = DEFAULT_STYLES[level]['style_begin']
		record.style_end   = DEFAULT_STYLES[level]['style_end']

		return super().format(record)
