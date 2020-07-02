import unittest
from parse import *
from sequence import *


class TestParsers(unittest.TestCase):

    # Reference: http://oeis.org/A000045
    @property
    def ref_id(self):
        self._ref_id = 'A000045'
        return self._ref_id

    # Reference: http://oeis.org/A139827
    @property
    def ref_id_six_digit(self):
        self._ref_id_six_digit = 'A139827'
        return self._ref_id_six_digit

    def test_parse_id_full(self):
        sequence = Sequence()
        id = 'A000045'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id, sequence.id)

    def test_parse_id_full_no_prefix(self):
        sequence = Sequence()
        id = '000045'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id, sequence.id)

    def test_parse_id_no_trailing_zeros(self):
        sequence = Sequence()
        id = 'A45'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id, sequence.id)

    def test_parse_id_no_trailing_zeros_no_prefix(self):
        sequence = Sequence()
        id = '45'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id, sequence.id)

    def test_parse_id_full_six_digit(self):
        sequence = Sequence()
        id = 'A139827'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id_six_digit, sequence.id)

    # Reference: http://oeis.org/A139827
    def test_parse_id_full_six_digit_no_prefix(self):
        sequence = Sequence()
        id = '139827'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id_six_digit, sequence.id)


if __name__ == '__main__':
    unittest.main()