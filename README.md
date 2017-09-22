# Pyteform

A python wrapper for the typeform api.

### Table of Contents

* [Installation](#installation)
* [Basic Usage](#basic-usage)
	* [Initialization](#initialization)
	* [Fetch all forms](#fetch-all-forms)
	* [Fetch questions](#fetch-questions)
	* [Fetch responses](#fetch-resposes)
	* [Fetch answers](#fetch-answers)
	* [Passing Filter Parameters](#passing-filter-parameters)
* [More Features](#more-features)
* [Contributing](#how-to-contribute)
* [License](#license)

### Installation

```sh
$ git clone https://github.com/m8r1x/pyteform.git
$ cd pyteform
$ pipenv install
$ python setup.py install

```

### Running Tests

The project uses [mock] and [nose] for tests.
To run the tests:
```sh
$ pipenv install --dev
$ cd tests
$ nosetests 
```

### Basic Usage

#### Initialization

```python
>>>
>>> from pyteform.api import Typeform
>>>
>>> api_key = "MY_API_KEY"
>>>
>>> tf = Typeform(api_key)
>>>
```

#### Fetch all forms

```python
>>>
>>> afdf = tf.all_forms() # if you're uncomfortable using dataframes pass param `format=list` to change return type to list
>>> type(afdf)
<class 'pandas.core.frame.DataFrame'>
>>> list(afdf)
['id', 'name']
>>> afdf.loc[0]
id                           O1Qb5c
name    VP of Engineering - Company
Name: 0, dtype: object
>>>
```

#### Fetch questions

```python
>>>
>>> qdf = tf.questions(afdf.id[5]) # params: `TYPEFORM_ID`, `format=list`(optional)
>>> type(qdf)
<class 'pandas.core.frame.DataFrame'>
>>> list(qdf)
['field_id', 'id', 'question']
>>> qdf.loc[3]
field_id                                             51801171
id                                             statement_EuEW
question    Within this application, we will require a 500...
Name: 3, dtype: object
>>>
```

#### Fetch responses

```python
>>>
>>> responses = tf.responses(afdf.id[7]) # params: `TYPEFORM_ID`
>>> type(responses)
<class 'list'>
>>> responses[0]
{'answers': {}, 'metadata': {'date_land': '2017-05-08 10:50:18', 'platform': 'other', 'referer': 'https://example.typeform.com/to/LYIEaV', 'network_id': '0a73a1c880', 'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30', 'date_submit': '0001-01-01 00:00:00', 'browser': 'default'}, 'completed': '0', 'token': 'df7024df014c95108987ec4823a9a0b1', 'hidden': []}
>>>
```

#### Fetch answers

```python
>>>
>>> ansdf = tf.answers(afdf.id[5]) # params: `TYPEFORM_ID`, `format=list`(optional)
>>> type(ansdf)
<class 'pandas.core.frame.DataFrame'>
>>> list(ansdf)
['dropdown_gSVo', 'email_jWBe', 'fileupload_HdwQ', 'fileupload_odoH', 'list_zUJ8_choice', 'textfield_C0No', 'textfield_QXiA', 'textfield_USJR', 'textfield_bpsU', 'textfield_fLIC', 'textfield_keTk', 'website_PTVG', 'website_PxQM', 'website_tzAL', 'website_v7W7']
>>>
>>> ansdf.loc[7]
dropdown_gSVo                                         In Between Jobs
email_jWBe                                      user@example.com
fileupload_HdwQ     https://api.typeform.com/v0/form/OXvQBJ/fields...
fileupload_odoH     https://api.typeform.com/v0/form/OXvQBXJ/fields...
list_zUJ8_choice                                       Other websites
textfield_C0No                                                User
textfield_QXiA                                      Software Engineer
textfield_USJR                                  Software Engineering
textfield_bpsU                                               User
textfield_fLIC                                                @user
textfield_keTk                                           0000000000
website_PTVG                   https://github.com/user/messenger
website_PxQM                             https://github.com/user
website_tzAL             https://www.linkedin.com/in/user/
website_v7W7                                    https://user.in/
Name: 7, dtype: object
>>>
```

#### Passing filter parameters

```python
>>>
>>> # pass a dictionary of filter options from those provided by the typeform api
>>> options = { 'completed': "true", 'limit': 10 }
>>> 
>>> tf.answers('TYPEFORM_ID', options=options)
>>>
```

### More features

#### Result distillation
Pyteform supports extra features such as distillation of results to filter out:
- emails
- file upload urls

To use this features, simply import the named functions from the `distil` module

```python
>>> 
>>> from pyteform.distil import email, file_upload_url
>>> 
>>> ansdf = tf.answers("TYPEFORM_ID") # results from typeform answers extraction
>>> 
>>> emails = email(ansdf)
>>> type(emails)
<class 'dict'>
>>> emails
{'email_37962684': ['test@typeform.com']}
>>> 
>>> 
>>> fu = file_upload_url(ansdf)
>>> type(fu)
<class 'dict'>
>>> fu
{'fileupload_37980234': ['https://api.typeform.com/v0/form/A8TcDI/fields/37980234/blob/c82215948b7
8-Cersei.jpg?key=664527c4c8bf2c6be6484b813e23e4f8ae066666']}
>>> 

```

### How to Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
2. Fork the repository on GitHub and create a branch `git checkout -b my-feature` for a feature or `git checkout -b bug-fix-bugname` for a bug fix to start making your changes.
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS.

### License

[MIT](https://opensource.org/licenses/MIT)

**Free software, Hell Yeah!**

[mock]: <https://github.com/testing-cabal/mock>
[nose]: <https://github.com/nose-devs/nose>
[pandas]: <https://github.com/pandas-dev/pandas>