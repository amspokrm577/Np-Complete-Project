import unittest
from maxclique import main as maxclique_
from unittest.mock import patch
from io import StringIO

class TestFiles(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def testWholeGraphIsMaxClique(self, mock_out):
        with patch('sys.stdin', new = StringIO(
        """15
        1 2
        1 3
        1 4
        1 5
        1 6
        2 3
        2 4
        2 5
        2 6
        3 4
        3 5
        3 6
        4 5
        4 6
        5 6
        """)):
            maxclique_()
        self.assertEqual(mock_out.getvalue(),
            '1 2 3 4 5 6\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testRandom1(self, mock_out):
        with patch('sys.stdin', new = StringIO(
       """41
        1 2
        1 3
        1 4
        1 5
        1 6
        1 7
        12 5
        12 8
        16 7
        13 8
        13 9
        14 6
        15 12
        16 2
        1 8
        2 3
        2 4
        2 5
        2 6
        2 7
        2 8
        3 4
        3 5
        3 6
        3 7
        3 8
        4 5
        4 6
        4 7
        4 8
        5 6
        5 7
        5 8
        6 7
        6 8
        7 8
        9 2
        10 4
        10 11
        11 4
        11 2
        """
        )):
            maxclique_()
        self.assertEqual(mock_out.getvalue(),
            '1 2 3 4 5 6 7 8\n')

    @patch('sys.stdout', new_callable=StringIO)
    def testZeroEdges(self, mock_out):
        with patch('sys.stdin', new = StringIO(
        """0
        """)):
            maxclique_()
        self.assertEqual(mock_out.getvalue(),
            'Not valid\n')



