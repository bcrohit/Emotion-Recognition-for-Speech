#!/usr/bin/env python
# coding: utf-8

# In[1]:


import predict as esf
import numpy as np
import joblib

# In[2]:


path = r"C:\Users\gowda\Downloads\the-fucking-movit-library-44332.mp3"

mfcc = esf.save_mfcc(path, 'mfcc', num_segments=3)
mels = esf.save_mfcc(path, 'mels', num_segments=3)
cqt = esf.save_mfcc(path, 'chroma_cqt', num_segments=3)
stft = esf.save_mfcc(path, 'chroma_stft', num_segments=3)


# In[6]:


def convert_to_2d(X):
    x = []
    for i in range(len(X)):
        x.append(X[i].flatten())
        
    return np.array(x)


# In[8]:


xmels = convert_to_2d(mfcc)
xmfcc = convert_to_2d(mels)
xstft = convert_to_2d(stft)
xcqt = convert_to_2d(cqt)


# In[11]:


xnew = np.concatenate((xmels, xmfcc, xstft, xcqt))
scale = RobustScaler()
x = scale.fit_transform(xnew)


# In[12]:


mlp_model = joblib.load(r"G:\My Drive\Models\mlp_model_rob.joblib")


# In[94]:





# In[95]:





# In[44]:


xmels = np.sum(xmels, axis=0)
xmfcc = np.sum(xmfcc, axis=0)
xstft = np.sum(xstft, axis=0)
xcqt = np.sum(xcqt, axis=0)


# In[9]:


xmels.shape


# In[13]:


p = mlp_model.predict(x)


# In[14]:


a, b = np.unique(p, return_counts=True)


# In[15]:


a, b


# In[98]:


a, b


# In[142]:


import matplotlib.pyplot as plt
plt.bar(a, b)
plt.gca().set_xscale('linear')
plt.show()


# In[104]:


import statistics as stats


# In[107]:


help(stats.mode)


# In[ ]:




