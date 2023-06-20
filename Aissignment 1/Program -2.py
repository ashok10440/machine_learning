#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
exp = [0.2, 0, 0, 0, 0, 0]
plt.pie(popularity, labels = languages, explode = exp, shadow = True, autopct='%1.1f%%', startangle = 135)
plt.show()


# In[ ]:




