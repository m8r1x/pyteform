from unittest import TestLoader, TextTestRunner, TestSuite
from .api_tests import TypeformTestCase
from .distil_tests import TestDistil

if __name__ == '__main__':
	loader = TestLoader()
	suite = TestSuite((
		loader.loadTestsFromTestCase(TypeformTestCase),
		loader.loadTestsFromTestCase(TestDistil)
		))

	runner = TextTestRunner(verbosity = 2)
	runner.run(suite)
