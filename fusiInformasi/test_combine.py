import unittest
import fusi

class TestFusionArray(unittest.TestCase):
    def test_combine(self):
        arrays = ['0000001001000000', '1000100010000000']
        actual = fusi._fusion(arrays)
        expected = ['1000101011000000']
        self.assertEqual(actual, expected)