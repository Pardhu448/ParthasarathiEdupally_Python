import unittest
import pandas as pd

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src import utils

class module_tests(unittest.TestCase):
    '''
    Tests for different funtions used in this module
    '''

    def test_caleodtransac(self):
        '''
        Tests if the function returns desired output for a sample input of transactions.
        input: Dataframe 
        assertion condition: output data frame should have zero EodQuantity
        '''
        input_dframe = pd.DataFrame({'Instrument' : ['IBM']*2, 
            'TransactionType': ['B', 'S'], 
            'AccountType': ['E', 'E'], 
            'TransactionQuantity': [1000, 1000], 
            'Quantity': [100000, -100000]})
        self.assertEqual(sum(utils.cal_eod_transac(input_dframe)['EodQuantity']), 0)

if __name__ == '__main__':

    unittest.main()


