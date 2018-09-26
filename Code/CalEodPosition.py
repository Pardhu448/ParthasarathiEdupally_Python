# This file contains sample usage code for this module.

from src import PosCalProcess

transac_date = '23-09-2018'

eod_23rdSep = PosCalProcess.Process(date = transac_date)


Eod_Pos_Dframe = eod_23rdSep.GetPositions()
print(Eod_Pos_Dframe)
print("This %s has lowest net transaction volume for the date - %s."%(eod_23rdSep.GetLowestVol(), transac_date))
print("This %s has largest net transaction volume for the date - %s"%(eod_23rdSep.GetLargestVol(), transac_date))


