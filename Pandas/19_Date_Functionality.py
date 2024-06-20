import pandas as pd
import numpy as np

print('Print date in 5 continious manner : ')
print(pd.date_range('1/1/2011', periods=5))
print()

print('Print date in 5 continious manner but period is month: ')
print(pd.date_range('1/1/2011', periods=5, freq='M'))
print()

print('Print date in 5 continious manner but period is year: ')
print(pd.date_range('1/1/2011', periods=5, freq='Y'))
print()



