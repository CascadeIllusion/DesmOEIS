import unittest
from parse import *
from sequence import *

"""
# Example sequences used:
http://oeis.org/A000045
http://oeis.org/A139827
"""


class TestIdParsing(unittest.TestCase):

    @property
    def ref_id(self):
        self._ref_id = 'A000045'
        return self._ref_id

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

    def test_parse_id_full_six_digit_no_prefix(self):
        sequence = Sequence()
        id = '139827'
        parse_id(id, sequence)
        self.assertEqual(self.ref_id_six_digit, sequence.id)


class TestIntegerParsing(unittest.TestCase):

    @property
    def ref_list(self):
        self._ref_list = ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144', '233', '377', '610',
                          '987', '1597', '2584', '4181', '6765', '10946', '17711', '28657', '46368', '75025', '121393',
                          '196418', '317811', '514229', '832040', '1346269', '2178309', '3524578', '5702887', '9227465',
                          '14930352', '24157817', '39088169', '63245986', '102334155']
        return self._ref_list

    def test_parse_integers(self):
        sequence = Sequence()
        id = 'A000045'
        parse_id(id, sequence)
        self.assertEqual(self.ref_list, sequence.integers)


class TestNameParsing(unittest.TestCase):

    @property
    def ref_name(self):
        self._ref_name = "t_e_s_t="
        return self._ref_name

    def test_parse_name(self):
        sequence = Sequence()
        id = 'A000045'
        parse_id(id, sequence)
        parse_name("test", sequence)
        self.assertEqual(self.ref_name, sequence.name)


if __name__ == '__main__':
    unittest.main()