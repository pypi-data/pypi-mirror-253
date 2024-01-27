import io
import json
import logging
import unittest

import nice_logging

class JsonFormatter(logging.Formatter):
	def format(self, record):
		if getattr(record, 'structured', False):
			message = record.msg
			data = record.structured_data
		else:
			message = super().format(record)
			data = {}

		return json.dumps({ '_message': message, **data })

class TestJsonOutput(unittest.TestCase):
	def setUp(self):
		self.stream = io.StringIO()
		handler = logging.StreamHandler(self.stream)
		handler.setFormatter(JsonFormatter())
		nice_logging.getLogger().handlers = [handler]
		self.logger = nice_logging.getStructuredLogger('json_logger')

	def get_output(self):
		return json.loads(self.stream.getvalue())

	def test_basic_types(self):
		self.logger.debug("A debug message!", i=42, s="foo", l=[1,2,3], o={'i':2, 's':'FILE_NOT_FOUND'}, n=None)
		j = self.get_output()

		self.assertEqual(j['_message'], "A debug message!")
		self.assertEqual(j['i'], 42)
		self.assertEqual(j['s'], "foo")
		self.assertEqual(j['l'], [1, 2, 3])
		self.assertEqual(j['o'], { 'i': 2, 's': 'FILE_NOT_FOUND' })
		self.assertEqual(j['n'], None)
