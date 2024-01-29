import unittest
from src.NBRB_bki_xml_read.individual_read import (
    read_latecount
)

class TestReadLatecount(unittest.TestCase):
    '''
    Testing NBRB_bki_xml_read.individual_read.read_latecount
    '''

    # here are lisr of optison that can be passed to funtion
    # and results corresponds to them
    options = [
        (
            [
                {'mindays': '1', 'maxdays': '7', 'count': '5'},
                {'mindays': '8', 'maxdays': '30', 'count': '2'},
                {'mindays': '31', 'maxdays': '60', 'count': '0'},
                {'mindays': '61', 'maxdays': '90', 'count': '0'},
                {'mindays': '91', 'maxdays': '180', 'count': '0'},
                {'mindays': '181', 'count': '0'}
            ],
            {
                '[1;7]': 5, '[8;30]': 2, '[31;60]': 0, 
                '[61;90]': 0, '[91;180]': 0, '>181': 0
            }
        ),
        (
            [
                {'mindays': '1', 'maxdays': '7', 'count': '5'},
                {'mindays': '12', 'maxdays': '32', 'count': '2'},
                {'mindays': '31', 'maxdays': '60', 'count': '2'},
                {'mindays': '12', 'maxdays': '91', 'count': '4'},
                {'mindays': '11', 'maxdays': '90', 'count': '5'},
                {'mindays': '23', 'count': '33'}                
            ],
            {
                '[1;7]': 5, '[12;32]': 2, '[31;60]': 2, 
                '[12;91]': 4, '[11;90]': 5, '>23': 33
            }
        )
    ]

    def test_read_latecount(self):
        '''
        Try different options and check that
        function returns the correct result.
        '''
        for option, result in self.options:
            self.assertEqual(
                read_latecount(option), result
            )
