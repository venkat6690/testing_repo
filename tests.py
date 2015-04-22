import unittest

from pydna import seq_utils


class TestSeqUtils(unittest.TestCase):
    def test_is_codon_correct(self):
        codon = 'ATC'
        result = seq_utils.is_codon_correct(codon)
        expected = True
        self.assertEqual(expected, result)

    def test_is_codon_correct_bad_codon1(self):
        codon = 3.1416
        result = seq_utils.is_codon_correct(codon)
        expected = False
        self.assertEqual(expected, result)

    def test_is_codon_correct_bad_codon2(self):
        codon = 'A*C'
        result = seq_utils.is_codon_correct(codon)
        expected = False
        self.assertEqual(expected, result)
