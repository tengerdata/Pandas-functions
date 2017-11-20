
import pandas as pd

df = pd.DataFrame({'A': [1,2,3,4], 'B': [5,6,7,8], 'C': [9,10,11,12]})

new_row = pd.DataFrame({'A': [35], 'B': [27], 'C': [43]})

df.loc[4] = new_row.loc[0]
print(df)

"""
Output:

    A   B   C
0   1   5   9
1   2   6  10
2   3   7  11
3   4   8  12
4  35  27  43
"""
