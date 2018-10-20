
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


def evalChisq(val):
    x = (2,2)
    X = np.zeros(x)
    values = np.array(val)
    for j in range(2):
        for i in range(2):
            X[i][j] = (values[i,:].sum()*values[:,j].sum())/((values).sum())
    return ((values-X)**2/X).sum()

