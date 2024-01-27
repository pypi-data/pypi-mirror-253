import contextlib
import io
import unittest

import nice_logging

class TestCustomFormats(unittest.TestCase):
	def setUp(self):
		self.stderr_ctx = contextlib.redirect_stderr(io.StringIO())
		self.stderr_capture = self.stderr_ctx.__enter__()

	def tearDown(self):
		self.stderr_ctx.__exit__(None, None, None)

	def get_output(self):
		return self.stderr_capture.getvalue()

	def test_format(self):
		nice_logging.basicConfig(force=True, level=nice_logging.DEBUG, format='MyCustomFormat<< %(message)s >>')
		logger = nice_logging.getLogger('test_logger')
		logger.debug('debugMessage! %s', 'stringParam!')

		self.assertEqual('MyCustomFormat<< debugMessage! stringParam! >>\n', self.get_output())

	def test_date_format(self):
		nice_logging.basicConfig(force=True, level=nice_logging.DEBUG, datefmt='MyDate<< %Y-%m-%d >>MyDate')
		logger = nice_logging.getLogger('test_logger')
		logger.debug('debugMessage! %s', 'stringParam!')

		self.assertIn('MyDate<<', self.get_output())
		self.assertIn('>>MyDate', self.get_output())

	def test_format_and_date_format(self):
		nice_logging.basicConfig(force=True, level=nice_logging.DEBUG, datefmt='<~date~>', format='[[%(asctime)s %(message)s]]')
		logger = nice_logging.getLogger('test_logger')
		logger.debug('debugMessage! %s', 'stringParam!')

		self.assertEqual('[[<~date~> debugMessage! stringParam!]]\n', self.get_output())
