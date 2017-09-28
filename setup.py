from setuptools import setup, find_packages

setup(
	name='pyteform',
	version='0.1.0-alpha',
	author="m8r1x",
	author_email="m8r1x.io@gmail.com",
	description="A python wrapper for the typeform api.",
	packages=find_packages(exclude=["*.tests", "*.tests.", "tests.*", "tests"]),
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
