
# coding: utf-8

# In[121]:

# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import numpy as np
# Enable inline plotting
get_ipython().magic('matplotlib inline')
from datetime import date


# In[122]:

df = pd.DataFrame({'A': [1,2,3,4], 'B': [5,6,7,8], 'C': [9,10,11,12]})
df


# In[123]:

new_row = pd.DataFrame({'A': [35], 'B': [27], 'C': [43]})
new_row


# In[124]:

df.loc[4] = new_row.loc[0]
print(df)


# In[ ]:



