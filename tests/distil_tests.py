import json
import unittest

from pyteform.distil import filter_emails, email, file_upload_url

def load_answers(file):
	import pandas as pd
	try:
		with open(file) as f:
			answers = json.load(f)
			ans = answers['responses'][2]['answers']
			df = pd.DataFrame([ans], columns=list(ans.keys()))
			return df
	except IOError as e:
		print("Error reading file!")

	return {}


class TestDistil(unittest.TestCase):
	""" Tests for `distil.py`. """
	def test_filter_emails(self):
		""" it should extract emails using regex """
		text = "I can extract your email@provider.domain from this text."
		email = filter_emails(text)
		assert "email@provider.domain" == email

	def test_email(self):
		""" it should return { 'field_id': ['email', ...] } """
		df = load_answers("mockapi/v1/form/TYPEFORM_ID.json")
		emails = email(df)
		assert emails['email_37962684'][0] == "test@typeform.com"

	def test_file_upload_url(self):
		""" it should return { 'field_id': ['file_upload_url', ...] } """
		df = load_answers("mockapi/v1/form/TYPEFORM_ID.json")
		file_upload_urls = file_upload_url(df)
		assert "Cersei.jpg" in file_upload_urls['fileupload_37980234'][0]

	def test_email_throws(self):
		""" it should throw TypeError given non (list or dataframe) params """
		self.assertRaises(TypeError, email, {})

	def test_file_upload_throws(self):
		""" it should throw TypeError given non (list or dataframe) params """
		self.assertRaises(TypeError, file_upload_url, {})

if __name__ == '__main__':
	unittest.main()
