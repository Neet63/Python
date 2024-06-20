# Pandas provide API to customize some aspects of its behavior

import pandas as pd
import numpy as np

# below are the five relavant function:
# 1. get_option()
# 2. set_option()
# 3. reset_option()
# 4. describe_option()
# 5. option_context()


# get_option() ->  takes a single parameter and returns the value as given in the output 
print('displays the rows with this value as upper limit to display : ', end='')
print(pd.get_option("display.max_rows"))
print('displays the columns with this value as upper limit to display : ', end='')
print(pd.get_option("display.max_columns"))

# display.max_columns = 0 -> pandas will not limit the number of columns displayed. 
print()


# set_option() -> can change the default number of rows to be displayed.
pd.set_option("display.max_row", 63)
pd.set_option("display.max_columns", 10)
print('After setting display.max_row : ',pd.get_option("display.max_row"))
print('After setting display.max_columns : ',pd.get_option("display.max_columns"))
print()


# reset_option() -> can change the value back to the default number of rows to be displayed.
pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")

print('After re-setting display.max_row : ',pd.get_option("display.max_row", 63))
print('After re-setting display.max_columns : ',pd.get_option("display.max_columns", 10))
print()


# describe_option() -> prints the description of the argument.
print('Description of display.max_rows : ')
print(pd.describe_option("display.max_rows"))


# option_context() -> used to set the option in with statement temporarily.
#                  -> Option values are restored automatically when you exit the with block 

with pd.option_context("display.max_rows",10):
   print('Inside the block : ',pd.get_option("display.max_rows"))
   print('Inside the block : ',pd.get_option("display.max_rows"))

print('Outside the block : ', pd.get_option("display.max_rows"))