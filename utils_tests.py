import unittest
from utils import Utils

class TestFunctions(unittest.TestCase):
	def test_reversed(self):
		# inputs and outputs are lists that contain a series of inputs with corresponding outputs
		inputs = [123, -6789, 15.2, "hi"]
		outputs = [321, -9876, None, None]
		for i, input in enumerate(inputs):
			reversed_num = Utils.reversed(input)
			self.assertEqual(reversed_num, outputs[i])

	def test_formatter(self):
		# input and binary_outputs, octal_outputs are lists that contain inputs with corresponding binary and octal outputs
		inputs = [123, -6789, 15.2, "hi"]
		binary_outputs = ['0b1111011', '-0b1101010000101', None, None]
		octal_outputs = ['0o173', '-0o15205', None, None]
		for i, input in enumerate(inputs):
			binary_num, octal_num = Utils.formatter(input)
			with self.subTest(name="Binary Test"):
				self.assertEqual(binary_num, binary_outputs[i])
			with self.subTest(name="Octal Test"):
				self.assertEqual(octal_num, octal_outputs[i])

if __name__ == "__main__":
    unittest.main()
