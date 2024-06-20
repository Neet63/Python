
import pandas as pd
import numpy as np
# rolling()
df = pd.DataFrame(np.random.randint(1,10,(10, 4)),
                  index = pd.date_range('1/1/2000', periods=10),
                  columns = ['A', 'B', 'C', 'D'])
print('Original Data Frame : ')
print(df)
print()


print('after rolling and mean : ')
print(df.rolling(window=3).mean())  # find mean of 3 cell including it and above it

# expanding() 
# min_period -> min cell of above to take 

print('After expanding : ')
print (df.expanding(min_periods=3).mean())


# ewm() -> 

print('EWM : ')
print(df.ewm(com=0.5).mean())