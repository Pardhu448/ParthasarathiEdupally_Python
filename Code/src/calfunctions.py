import pandas as pd 

def cal_eod_transac(groupxy):
    '''
    Calculated eod transaction quantity and delta of transaction quantity 
    for each instrument and returns DataFrame with all this information.
    '''

    gr_type = set(groupxy['AccountType'])
    
    if (gr_type <= {'E'}):
        type_mask = {'S': -1, 'B': 1}
    elif (gr_type <= {'I'}):
        type_mask = {'S': 1, 'B': -1}
    else:
        try:
            raise Exception('No DataFrame after merging.')
        except Exception as e:
            print(str(e) + 'Something wrong with merging Transactions and Positions data,' + 'none of the required type (EB, ES, IB, IS) after merge.')
         
    groupxy = groupxy.replace({'TransactionType' : type_mask})
    
    groupxy['TransactionQuantity'] = groupxy['TransactionQuantity'] * groupxy['TransactionType']
    
    eod_dframe = groupxy.groupby(['Instrument', 'AccountType', 
                                  'Quantity']).apply(lambda x: sum(x['TransactionQuantity'])).reset_index()
    
    eod_dframe['EodQuantity'] = eod_dframe['Quantity'] + eod_dframe[0]
    eod_dframe['Delta'] = eod_dframe[0]
    
    return eod_dframe[['EodQuantity', 'Delta']]

def combine_data(pos_data, transac_data):
    '''
    Checks for transaction history for all the instruments in positions data.
    Replaces NAs of positions having no transactions with zero 
    and 'S' appropriately. Returns merged dataframe useful for quickly calculate 
    Eod transaction quantity.
    '''
    pos_instru = set(pos_data['Instrument'].unique())
    transac_instru = set(transac_data['Instrument'].unique())

    if (pos_instru - transac_instru):
        print('Following intruments dont have transaction history for the day: %s'% pos_instru.difference(transac_instru))
    else:
        print('All positions have transaction history for the day')

    merged_data = pos_data.merge(transac_data, how = 'outer', on = 'Instrument')
    merged_data.TransactionQuantity = merged_data.TransactionQuantity.fillna(0)
    merged_data.TransactionType = merged_data.TransactionType.fillna('S')
    return merged_data

