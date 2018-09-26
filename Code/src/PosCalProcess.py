import pandas as pd
from src import core, TransacData

class Process(core.process):
    '''
    Interface class for performing position calculations, 
    getting lowest and largest net volume instruments etc.
    It uses 'process' class from 'core' module as base.
    '''
       
    def GetPositions(self, **kwargs):
        '''
        Returns a DataFrame with information about EoD positions 
        and Delta for a given time period.
        '''
        return self.data.snapshot

    def GetLowestVol(self, **kwargs):
        '''
        Returns an Instrument with lowest net Volume in a given time 
        period.
        '''
        return self.data.snapshot.loc[self.data.snapshot['Delta'].apply(lambda x: abs(x)).idxmin()]

    def GetLargestVol(self, **kwargs):
        '''
        Returns an Instrument with largest net Volume in a given time
        period.
        '''
        return self.data.snapshot.loc[self.data.snapshot['Delta'].apply(lambda x: abs(x)).idxmax()]    
        
    def __init__(self, date, **kwargs):
        
        self.date = date
        data = TransacData.Transactions(date, **kwargs)
        core.process.__init__(self, data)

