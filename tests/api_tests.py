import json
import sys
import unittest

from mock import patch
from os.path import normpath
from urllib.parse import urlparse

sys.path.append('..')
from pyteform import Typeform

def mock_urlopen(url):
	""" 
		A stub get_form() implementation that loads
		responses from the filesystem.
	"""
	# Map path from url to file
	parsed_url = urlparse(url)
	payload_file = normpath("mockapi%s.json" % parsed_url.path)
	# Must return a file like object
	return open(payload_file, mode='rb')

class TypeformTestCase(unittest.TestCase):
	""" Tests for `api.py`. """
	def setUp(self):
		self.patcher = patch('pyteform.api.urlopen', mock_urlopen)
		self.patcher.start()
		self.typeform = Typeform("API_KEY")

	def tearDown(self):
		self.patcher.stop()

	def test_questions(self):
		""" Question column exists questions dataframe"""
		questions = self.typeform.questions("TYPEFORM_ID")
		assert 'question' in questions.columns

	def test_answers(self):
		""" Answers column exists in answers dataframe """
		answers = self.typeform.answers("TYPEFORM_ID")
		assert 'answers' in answers.columns

if __name__ == '__main__':
	unittest.main()