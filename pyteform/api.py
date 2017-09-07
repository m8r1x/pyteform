import json
import pandas as pd

from urllib.request import urlopen

def get_form(api_key, typeform_id, **options):
	typeform_url = "https://api.typeform.com/v1/form/"
	typeform_url += str(typeform_id) + "?key=" + str(api_key)
	
	filters = ['completed', 'limit', 'offset', 'order_by', 'order_by[]', 'since', 'token', 'until']

	if options:
		for key, value in options.items():
			if key not in filters: continue
			typeform_url += '&{0}={1}'.format(key, value)

	response = urlopen(typeform_url)
	raw_data = response.read().decode('utf-8')
	return json.loads(raw_data)

	
class Typeform:
	def __init__(self, api_key):
		self.api_key = str(api_key)

	def all_forms(self):
		typeform_url = "https://api.typeform.com/v1/forms?key="
		typeform_url += self.api_key
		api_response = urlopen(typeform_url)
		raw_data = api_response.read().decode('utf-8')
		json_data = json.loads(raw_data)
		typeform_df = pd.DataFrame(json_data)
		return typeform_df

	def answers(self, typeform_id, **options):
		typeform_responses = self.responses(typeform_id, **options)
		typeform_answers = [response['answers'] for response in typeform_responses if 'answers' in response]
		typeform_answers = [answer for answer in typeform_answers if answer != {}]
		answers_df = pd.DataFrame(typeform_answers)
		return answers_df

	def questions(self, typeform_id, **options):
		api_response = get_form(self.api_key, typeform_id, **options)
		qs = api_response['questions']
		questions_df = pd.DataFrame(qs)
		return questions_df

	def responses(self, typeform_id, **options):
		api_response = get_form(self.api_key, typeform_id, **options)
		typeform_responses = api_response['responses']
		return typeform_responses