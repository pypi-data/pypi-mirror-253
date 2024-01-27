import contextlib
import io
import unittest

import nice_logging

class TestBasicOutput(unittest.TestCase):
	def setUp(self):
		self.stderr_ctx = contextlib.redirect_stderr(io.StringIO())
		self.stderr_capture = self.stderr_ctx.__enter__()
		nice_logging.basicConfig(force=True, level=nice_logging.TRACE)
		self.logger = nice_logging.getLogger('test_logger')

	def tearDown(self):
		self.stderr_ctx.__exit__(None, None, None)

	def get_output(self):
		return self.stderr_capture.getvalue()

	def test_critical(self):
		self.logger.critical('criticalMessage!')
		self.assertIn('criticalMessage!', self.get_output())

	def test_error(self):
		self.logger.error('errorMessage!')
		self.assertIn('errorMessage!', self.get_output())

	def test_warning(self):
		self.logger.warning('warningMessage!')
		self.assertIn('warningMessage!', self.get_output())

	def test_info(self):
		self.logger.info('infoMessage!')
		self.assertIn('infoMessage!', self.get_output())

	def test_debug(self):
		self.logger.debug('debugMessage!')
		self.assertIn('debugMessage!', self.get_output())

	def test_trace(self):
		self.logger.trace('traceMessage!')
		self.assertIn('traceMessage!', self.get_output())

	def test_message_parameters(self):
		self.logger.debug("This: %d %s", 9990420999, 'stringParam')
		self.assertIn('9990420999', self.get_output())
		self.assertIn('stringParam', self.get_output())

	def test_unthrown_exception_info(self):
		class MyUnthrownException(Exception): pass
		e = MyUnthrownException('unthrownException!')
		self.logger.warning("Not thrown:", exc_info=e)
		self.assertIn('MyUnthrownException', self.get_output())
		self.assertIn('unthrownException!', self.get_output())

	def test_exception_info(self):
		class MyException(Exception): pass
		try:
			raise MyException('myException!')
		except Exception as e:
			self.logger.error("Thrown:", exc_info=e)

		self.assertIn('MyException', self.get_output())
		self.assertIn('myException!', self.get_output())
