import json
import pandas as pd

try:
	from urllib.request import urlopen
	from urllib.error import URLError, HTTPError
except ImportError:
	from urllib2 import urlopen, URLError, HTTPError

	
def get_form(api_key, typeform_id, options=None):
	typeform_url = "https://api.typeform.com/v1/form/"
	typeform_url += str(typeform_id) + "?key=" + str(api_key)
	
	filters = ['completed', 'limit', 'offset', 'order_by', 'order_by[]', 'since', 'token', 'until']

	if options:
		if not isinstance(options, dict):
			raise TypeError("Options must be a dictionary!")
		for key, value in options.items():
			if key not in filters: continue
			typeform_url += '&{0}={1}'.format(key, value)

	try:
		response = urlopen(typeform_url)
		raw_data = response.read().decode('utf-8')
		return json.loads(raw_data)
	except HTTPError as e:
		print("HTTPError: %s" % e.code)
	except URLError as e:
		print("URLError: %s" % e.reason)
	except Exception:
		import traceback
		print("generic exception: {0}".format(traceback.format_exc()))

	return {}

def keyerror(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except KeyError as e:
			print("Key not found!")
	return wrapper


class Typeform:
	def __init__(self, api_key):
		self.api_key = api_key

	def all_forms(self, format=None):
		typeform_url = "https://api.typeform.com/v1/forms?key="
		typeform_url += str(self.api_key)
		api_response = urlopen(typeform_url)
		raw_data = api_response.read().decode('utf-8')
		json_data = json.loads(raw_data)
		if format is list: return json_data
		typeform_df = pd.DataFrame(json_data)
		return typeform_df

	@keyerror
	def answers(self, typeform_id, format=None, options=None):
		typeform_responses = self.responses(typeform_id, options)
		typeform_answers = [response['answers'] for response in typeform_responses if 'answers' in response]
		typeform_answers = [answer for answer in typeform_answers if answer != {}]
		if format is list: return typeform_answers
		answers_df = pd.DataFrame(typeform_answers)
		return answers_df

	@keyerror
	def questions(self, typeform_id, format=None, options=None):
		api_response = get_form(self.api_key, typeform_id, options)
		qs = api_response['questions']
		if format is list: return qs
		questions_df = pd.DataFrame(qs)
		return questions_df

	@keyerror
	def responses(self, typeform_id, options=None):
		api_response = get_form(self.api_key, typeform_id, options)
		typeform_responses = api_response['responses']
		return typeform_responses
