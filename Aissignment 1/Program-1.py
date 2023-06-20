#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Create a random vector of size 15 with integers in the range of 1-20
random_vector = np.random.randint(1, 21, size=15)

# Print the random vector
print("Random vector:")
print(random_vector)


# In[2]:


import numpy as np

# Create a random vector of size 15 with integers in the range of 1-20
random_vector = np.random.randint(1, 21, size=15)

# Reshape the array to a 3 by 5 array
reshaped_array = random_vector.reshape(3, 5)

# Print the reshaped array
print("Reshaped array:")
print(reshaped_array)


# In[3]:


import numpy as np

# Create a random vector of size 15 with integers in the range of 1-20
random_vector = np.random.randint(1, 21, size=15)

# Reshape the array to a 3 by 5 array
reshaped_array = random_vector.reshape(3, 5)

# Print the shape of the reshaped array
print("Shape of the array:", reshaped_array.shape)


# In[4]:


# Replace the maximum value in each row with 0
reshaped_array[np.arange(len(reshaped_array)), np.argmax(reshaped_array, axis=1)] = 0

# Print the resulting array
print("Resulting array:")
print(reshaped_array)


# In[5]:


# Replace the maximum value in each row with 0
reshaped_array[np.arange(len(reshaped_array)), np.argmax(reshaped_array, axis=1)] = 0

# Print the resulting array
print("Resulting array:")
print(reshaped_array)


# In[6]:


import numpy as np

# Create a 2-dimensional array of size 4 x 3 with 4-byte integer elements
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.int32)

# Print the shape of the array
print("Shape of the array:", array.shape)

# Print the type of the array
print("Type of the array:", type(array))

# Print the data type of the array
print("Data type of the array:", array.dtype)


# In[7]:


import numpy as np

# Define the array
arr = np.array([[3, -2], [1, 0]])

# Compute the eigenvalues and right eigenvectors
eigenvals, eigenvects = np.linalg.eig(arr)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:", eigenvals)
print("Right Eigenvectors:")
print(eigenvects)


# In[8]:


import numpy as np

# create array
my_array = np.array([[0, 1, 2], [3, 4, 5]])

# compute sum of diagonal elements
diag_sum = np.trace(my_array)

# print result
print("Sum of diagonal elements:", diag_sum)


# In[9]:


m = np.arange(1,7).reshape(3,2)
m = m.reshape(2,3)
m


# In[ ]:




