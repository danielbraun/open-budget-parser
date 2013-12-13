import unittest
from datetime import date
from parser import parse_rtf

class ParserTests(unittest.TestCase):
    def setUp(self):
        self.committee_file = 'rtf/2007-04-29-01.rtf'

    def test_parse_rtf(self):
        result = parse_rtf(self.committee_file)
        expected = {
            'date': date(2007, 4, 29),
            'clauses': [168, 182, 183, 184, 185, 186, 187,
                         188, 189, 190, 191, 192, 193, 92]
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
