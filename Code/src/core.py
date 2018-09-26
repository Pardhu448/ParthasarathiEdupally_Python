import pandas as pd 

class transaction:
    '''
    Base class to contain methods for 
    manipulating "transaction" objects
    '''
    def __init__(self, snapshot = None, history = None):
        self.snapshot = snapshot
        self.history = history

    def __add__(self, other):
        '''
        Addition of two transaction objects is just combining two snapshot of 
        transactions through addition of transactions
        '''
        pass

    def __sub__(self):
        pass
    
class process:
    '''
    Base class to contain  methods for manipulating "Process" objects.
    '''
    def __init__(self, data):
        self.data = data


    def __add__(self, other):
        '''
        Addition of two processes gives new process whose transactions 
        are sum of transactions from both processes.
        '''
        pass

    def __sub__(self, other):
        pass

