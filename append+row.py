
import pandas as pd

df = pd.DataFrame({'A': [1,2,3,4], 'B': [5,6,7,8], 'C': [9,10,11,12]})

new_row = pd.DataFrame({'A': [35], 'B': [27], 'C': [43]})

df.loc[4] = new_row.loc[0]
print(df)
