#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[99]:


s_1=[0] 
x_M=[0]
T_1=[0]
gamma= 1.4
R = 287
cp = 1005 
To= 300
x =0
while x<3.5 and x>= 0 : 
    M = x+.1 
    x = M
    T = (2*cp *To)/(gamma *R*(M**2)+2*cp)
    s = ((cp/gamma)*(math.log(T)))+((R/2)*(math.log(To-T)))  
    T_1.append(T)
    s_1.append(s)
    x_M.append(M)
    


# In[100]:


x_M.remove(0)
T_1.remove(0)
s_1.remove(0)
x1 = np.array(s_1)
y1 = np.array(T_1)
plt.figure(figsize=(23,10))
plt.plot(x1, y1)
plt.title("Fanno line Graphical Formulation")
plt.xlabel("s")
plt.ylabel("h")
plt.show()


# In[101]:


dict = {'s':s_1,
        'T':T_1,
        'M' :x_M}
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
print(df)

