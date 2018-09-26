# PositionCalProcess for ABC Bank

This module calculates EoD positions of given instruments based on transactions in a given day.

## Getting Started
Steps to use this module:
1. Download the repository into local machine
2. Creating virual evironment (This step note required if using Anaconda Python3):
   - Make sure to create virtual environment using conda with file requirements.yml
   - *command:* conda env create -f requirements.yml

3. Populate both input files into data directory 
4. Run sample usage file **'CalEodPosition.py'**


```python
#To query instruments with largest and lowest net transaction volume 

from src import PosCalProcess 

transac_date = '23-09-2018'
sep23rd_process = ProcCalProcess.Process(date = transac_date)

sep23rd_snapshot  = sep23rd_process.GetPositions()
print(sep23rd_snapshot.GetLowestVol())
print(sep23rd_snapshot.GetLargetstVol())
```

## Requirements
1. Anaconda Python3

## Running the tests

1. test_caleodtransac : To test function 'cal_eod_transac' function with dummy input. 

2. *To run:*  python tests/module_tests.py -v

## Future extension

Classes are designed to accomodate future extension to aggregate 'Process' objects for calculating Eod transaction status considering past dates or range of dates also.

Also basic unit of computation is on pandas dataframes as it is effecient and can be parallelized with apply.

