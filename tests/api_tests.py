import json
import sys
import unittest

from mock import patch
from os.path import normpath

sys.path.append('..')
from pyteform import Typeform

def mock_urlopen(url):
	""" 
		A stub get_form() implementation that loads
		responses from the filesystem.
	"""
	try:
		from urllib.parse import urlparse
	except ImportError:
		from urlparse import urlparse
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
		"""  `questions` fields exist in a questions dataframe"""
		question_keys = ["id", "question", "field_id"]
		questions = self.typeform.questions("TYPEFORM_ID")
		for key in question_keys:
			assert key in questions.columns

	def test_answers(self):
		"""  `answers` fields exist in an answers dataframe """
		answer_keys = ["textfield_37671344", "date_37962697", "email_37962684",
		"textarea_37671420", "website_37962927", "yesno_37977952",
		"terms_37962909", "dropdown_37671567", "listimage_37967229_choice",
		"rating_37977395", "rating_37977403", "rating_37977401",
		"rating_37977400","list_37963973_choice","opinionscale_37979723",
		"fileupload_37980234","number_37980157","payment_37962979_price"]

		answers = self.typeform.answers("TYPEFORM_ID")
		for key in answer_keys:
			assert key in answers.columns

	def test_responses(self):
		"""  `responses` fields exist in a responses dictionary """
		response_keys = ["completed", "token", "metadata", "hidden", "answers"]
		responses = self.typeform.responses("TYPEFORM_ID")
		for key in response_keys:
			assert key in responses[0]

	def test_all_forms(self):
		""" `all forms` fields exist in an all_forms dataframe"""
		all_forms_keys = ["id", "name"]
		all_forms = self.typeform.all_forms()
		for key in all_forms_keys:
			assert key in all_forms.columns

if __name__ == '__main__':
	unittest.main()