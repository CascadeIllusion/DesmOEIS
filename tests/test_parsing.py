import unittest
from parsing import *
from sequence import *

"""
# Example sequences used:
http://oeis.org/A000045
http://oeis.org/A000047
http://oeis.org/A139827
"""


class TestIdParsing(unittest.TestCase):

    def test_parse_id(self):
        args = {"id": "A000045"}
        self.assertEqual("A000045", parse_id(args))

    def test_parse_id_no_prefix(self):
        args = {"id": "000045"}
        self.assertEqual("A000045", parse_id(args))

    def test_parse_id_no_trailing_zeros(self):
        args = {"id": "A45"}
        self.assertEqual("A000045", parse_id(args))

    def test_parse_id_no_trailing_zeros_no_prefix(self):
        args = {"id": "45"}
        self.assertEqual("A000045", parse_id(args))

    def test_parse_id_six_digit(self):
        args = {"id": "A139827"}
        self.assertEqual("A139827", parse_id(args))

    def test_parse_id_six_digit_no_prefix(self):
        args = {"id": "139827"}
        self.assertEqual("A139827", parse_id(args))


class TestIdFinding(unittest.TestCase):

    def test_find_id_success(self):
        id = "A000045"
        self.assertNotEquals(None, find_id(id))

    def test_find_id_fail(self):
        id = "A123ABC"
        self.assertEquals(None, find_id(id))


class TestIntegerParsing(unittest.TestCase):

    def test_parse_integers(self):
        args = {"": ""}
        id = "A000045"
        integers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
                    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
                    5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
        integers = list(map(str, integers))

        url = f"https://oeis.org/search?q=id:{id}&fmt=text"
        r = requests.get(url)

        sequence = Sequence(id)
        sequence.integers = integers
        sequence.results = r
        sequence.args = args

        self.assertEquals(integers, parse_integers(sequence))

    # Use a different sequence because most extended sequences are too big to reasonably fit
    def test_parse_integers_ext(self):
        args = {"ext": "true"}
        id = "A000047"
        integers = [1, 2, 3, 5, 8, 15, 26, 48, 87, 161, 299, 563, 1066, 2030, 3885, 7464, 14384, 27779, 53782, 104359,
                    202838, 394860, 769777, 1502603, 2936519, 5744932, 11249805, 22048769, 43248623, 84894767,
                    166758141, 327770275, 644627310, 1268491353, 2497412741, 4919300031, 9694236886, 19112159929]
        integers = list(map(str, integers))

        url = f"https://oeis.org/search?q=id:{id}&fmt=text"
        r = requests.get(url)

        sequence = Sequence(id)
        sequence.integers = integers
        sequence.results = r
        sequence.args = args

        self.assertEquals(integers, parse_integers(sequence))


if __name__ == '__main__':
    unittest.main()