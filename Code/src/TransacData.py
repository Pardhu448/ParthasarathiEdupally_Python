import pandas as pd 
from src import core, utils
from os.path import isfile, join
from os import listdir

class Transactions(core.transaction):
    ''' 
    Class to store transaction data at a time stamp
    for a particular instrument. Contains attributes like Initial Position, 
    Account Type, Net Transaction, Transaction History etc for a particular
    Instrument.
    '''
    
    @staticmethod
    def get_file(file_path):
        '''
        Check if all the input files required for calculations are 
        available and return the file as dataframe.
        '''
        files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
        if (len(files) > 1):
            try:
                raise Exception ('More than one file found in folder')
            except Exception as e:
                print(str(e) + 'at folder: %s'% file_path)        
        else:
            try:
                return pd.read_csv(file_path + '/' + files[0])
            except Exception:
                return pd.read_json(file_path + '/' + files[0])
    
    def get_snapshot(self, **kwargs):
        '''
        Returns multi-indexed series of 'TransacInfo' objects
        for a given date.
        '''
        transac_file_path = 'data/transactions'
        pos_file_path = 'data/positions'
        transactions_data = Transactions.get_file(transac_file_path)
        positions_data = Transactions.get_file(pos_file_path)
        
        merged_data = utils.combine_data(positions_data, transactions_data)

        snap_eod = merged_data.groupby(['Instrument', 
            'AccountType']).apply(utils.cal_eod_transac).reset_index()
        snap_eod = snap_eod.rename(columns = {'EodQuantity' : 
            'Quantity'}).drop(['level_2'], axis = 1)
        
        return snap_eod

    def get_net_transaction(self, **kwargs):
        '''
        Returns net volume bought out of Buy/Sell transactions 
        for a particular instrument.
        '''
        pass

    def get_transac_history(self, **kwargs):
        '''
        Returns transaction history for each intrument using transactions data.
        '''
        transac_file_path = 'data/transactions'
        transactions_data = Transactions.get_file(transac_file_path)

        return transactions_data

    def __init__(self, date, **kwargs):
        
        self.date = date
        history = self.get_transac_history(**kwargs)
        snapshot = self.get_snapshot(**kwargs)
        core.transaction.__init__(self, snapshot = snapshot, history = history)

