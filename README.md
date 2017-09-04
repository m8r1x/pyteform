# Pyteform
A python wrapper for the typeform api.

### Prerequisites
- python3
- pandas

### Installation
```
git clone https://github.com/m8r1x/pyteform.git
cd pyteform
python3 setup.py install

```

### Basic Usage
```python
from pyteform import Typeform

api_key = "MY_API_KEY"

typeform = Typeform(api_key)

# all methods return a pandas dataframe
typeform.all_forms()  # get all forms
typeform.questions('TYPEFORM_ID') # fetch all questions from a typeform
typeform.answers('TYPEFORM_ID') # fetch all answers from a typeform

# pass as many filter options from those provided by the typeform api
# in the form `filter_option=filter_value` as additional parameters
typeform.answers('TYPEFORM_ID', completed="true", limit=10)
```
