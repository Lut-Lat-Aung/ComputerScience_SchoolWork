#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform
from statsmodels.formula.api import ols

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


# In[2]:


nd = pd.read_csv("newData.csv")
nd.head()


# In[3]:


tc = pd.read_csv("telecom_churn.csv")
tc.head()


# In[5]:


t1 = pd.read_csv("train_1.csv")
t1.head()


# In[6]:


t2 = pd.read_csv("train_2.csv")
t2.head()


# In[ ]:




