import re
import pandas

def filter_emails(data):
	x = re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+', data)
	if x:
		return x.group()
	
def email(df):
	if not isinstance(df, pandas.core.frame.DataFrame):
		if not isinstance(df, list):
			raise TypeError("Cannot convert to DataFrame!")
		df = pandas.DataFrame(df)

	emails = dict()
	column_names = list(df)

	for name in column_names:
		column = df[name].tolist()
		email_list = list(filter(filter_emails, column))
		if email_list == []: continue
		emails[name] = email_list

	return emails

def file_upload_url(df):
	if not isinstance(df, pandas.core.frame.DataFrame):
		if not isinstance(df, list):
			raise TypeError("Cannot convert to DataFrame!")
		df = pandas.DataFrame(df)

	file_upload_urls = list()
	df_to_dict_list = df.to_dict(orient='list')

	for key in list(df_to_dict_list):
		x = re.search('fileupload_\w+', key)
		if not x:
			df_to_dict_list.pop(key, None)

	return df_to_dict_list