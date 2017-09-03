from setuptools import setup, find_packages

setup(
	name='pyteform',
	version='0.1.0-alpha',
	packages=find_packages(),
	license='MIT',
	install_requires=[
		'pandas'
	],
	test_require=[
		'nose',
		'mock'
	],
	long_description=open('README.md').read()
)