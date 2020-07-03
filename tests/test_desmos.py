import unittest
from desmos import *
from sequence import *

"""
# Example sequences used:
http://oeis.org/A000045
"""

class TestDesmos(unittest.TestCase):

    @property
    def ref_list(self):
        self._ref_list = ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144', '233', '377', '610',
                          '987', '1597', '2584', '4181', '6765', '10946', '17711', '28657', '46368', '75025', '121393',
                          '196418', '317811', '514229', '832040', '1346269', '2178309', '3524578', '5702887', '9227465',
                          '14930352', '24157817', '39088169', '63245986', '102334155']
        return self._ref_list

    def test_create_expression(self):
        sequence = Sequence()
        create_expression(self.ref_list, sequence, create_desmos_list)
        graph = open("A000045.html")
        graph = graph.read()
        self.assertEqual(graph, sequence.graph)

    def test_create_desmos_list(self):
        desmos_list = str(self.ref_list)
        desmos_list = desmos_list.replace("'", "")
        expr = f"calculator.setExpression({{ id: 'graph1', latex:\"{desmos_list}\" }});"
        self.assertEqual(create_desmos_list(self.ref_list), expr)