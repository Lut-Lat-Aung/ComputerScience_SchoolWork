#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


from sklearn.module import Model
model = Model()
model.fit(X,y)
predictions = model.predict(X_new)
print(predictions)


# In[5]:


import pandas as pd
import numpy as np

churn_df = pd.read_csv("churn_df.csv")

from sklearn.neighbors import KNeighborsClassifier
X = churn_df[["total_day_charge", "total_eve_charge"]].values
y = churn_df["churn"].values
print(X.shape, y.shape)


# In[6]:


knn = KNeighborsClassifier(n_neighbors = 15)
knn.fit(X,y)


# In[7]:


X_new = np.array([[56.8,17.5],
                 [24.4,24.1],
                 [50.1, 10.9]])

print(X_new.shape)


# In[8]:


predictions = knn.predict(X_new)
print("Prediction: {}".format(predictions))

    


# In[9]:


import pandas as pd
import numpy as np

churn_df = pd.read_csv("churn_df.csv")

from sklearn.neighbors import KNeighborsClassifier
X = churn_df[["total_day_charge", "total_eve_charge"]].values
y = churn_df["churn"].values
print(X.shape, y.shape)

knn = KNeighborsClassifier(n_neighbors = 15)
knn.fit(X,y)

X_new = np.array([[30.0,17.5],
                 [107.0,24.1],
                 [213.0, 100.9]])

print(X_new.shape)

predictions = knn.predict(X_new)
print(f"Prediction: {predictions}")


# In[10]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,
                                                   random_state = 21,
                                                   stratify=y)
knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))


# In[11]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,
                                                   random_state = 21,
                                                   stratify=y)
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))


# In[12]:


import matplotlib.pyplot as plt


train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,26)
print(neighbors)
for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors = neighbor)
    knn.fit(X_train, y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)
    
#print(train_accuracies.values())
print(test_accuracies.values())
my_train = list(train_accuracies.values())
my_test = list(test_accuracies.values())

plt.figure(figsize=(8,6))
plt.title("KNN: Varing Number of Neighbors")
plt.plot(neighbors, my_train, label="Training Accuracy")
plt.plot(neighbors, my_test, label="Tesing Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()


# In[13]:


#Exercise

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X = df.drop('churn', axis=1).values
y = df['churn'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
accuracy = knn.score(X_test, y_test)
print("Accuracy of the KNN model on the test data:", accuracy)


# In[ ]:


import matplotlib.pyplot as plt


train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,13)
print(neighbors)
for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors = neighbor)
    knn.fit(X_train, y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)
    
#print(train_accuracies.values())
print(test_accuracies.values())
my_train = list(train_accuracies.values())
my_test = list(test_accuracies.values())

plt.figure(figsize=(8,6))
plt.title("KNN: Varing Number of Neighbors")
plt.plot(neighbors, my_train, label="Training Accuracy")
plt.plot(neighbors, my_test, label="Tesing Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()


# In[ ]:


import pandas as pd

diabetes_df = pd.read_csv("diabetes.csv")
print(diabetes_df.head())

import pandas as pd


print("Initial Shape:", diabetes_df.shape)

diabetes_df = diabetes_df[diabetes_df['bmi'] != 0]

print("Shape after Subset for BMI not equal to 0:", diabetes_df.shape)

diabetes_df = diabetes_df[diabetes_df['glucose'] != 0]
print("Shape after Subset for Glucose not equal to 0:", diabetes_df.shape)

diabetes_df.head()



X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values

print(type(X), type(y))

X_bmi = X[:, 3]
print(y.shape, X_bmi.shape)

X_bmi = X_bmi.reshape(-1, 1)
print(X_bmi.shape)



import matplotlib.pyplot as plt
plt.scatter(X_bmi,y, color="Blue")
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel("Blood Mass Index")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.scatter(X_bmi, y, color="Red")
plt.plot(X_bmi, predictions)
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel("Body Mass Index")
plt.show()


# In[14]:


import pandas as pd
import numpy as np
sales_df = pd.read_csv('sales_df.csv')

X = sales_df['radio'].values
y = sales_df['sales'].values

X = X.reshape(-1, 1)
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)


# In[15]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Five prediction values:", predictions[:5])


# In[16]:


import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Actual Observations')

plt.plot(X, predictions, color='red', label='Linear Regression Model')

plt.xlabel('Radio Advertising Expenditure')
plt.ylabel('Sales')
plt.legend(loc='best')
plt.show()


# In[24]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3,
                                                   random_state = 42)

reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)

reg_all.score(X_test, y_test)

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared = False)

    


# In[18]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

X = sales_df.drop('sales', axis=1).values
y = sales_df['sales'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("First two values of y_pred:", y_pred[:2])
print("First two values of y_test:", y_test[:2])

r_squared = r2_score(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R-squared:", r_squared)
print("Root Mean Squared Error (RMSE):", rmse)


# In[19]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

reg_all = LinearRegression()
reg_all.fit(X_train, y_train)

y_pred = reg_all.predict(X_test)


# In[20]:


reg_all.score(X_test, y_test)


# In[21]:


from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared = False)


# In[29]:



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

sales_df = pd.read_csv('sales_df.csv')

X = sales_df.drop(columns=['sales'])  
y = sales_df['sales']               

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted values:", y_pred[:2])
print("Actual target :", y_test[:2])

r_squared = r2_score(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print()

print("R-squared:", r_squared)
print("Root Mean Squared Error (RMSE):", rmse)


# In[32]:


from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits = 6, shuffle=True, random_state=42)
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y , cv = kf)

print(cv_results)
print(np.mean(cv_results), np.std(cv_results))


# In[ ]:





# In[53]:


import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression

sales_df = pd.read_csv('sales_df.csv')

X = sales_df[['radio', 'social_media']]  
y = sales_df['sales']                   

kf = KFold(n_splits=6, shuffle=True, random_state=5)

reg = LinearRegression()
cv_scores = cross_val_score(reg, X, y, cv=kf)

print("CV scores: ", cv_scores)

mean_score = np.mean(cv_scores)
print("Mean:", mean_score)

std_score = np.std(cv_scores)
print("Std:", std_score)

confidence_interval = np.quantile(cv_scores, [0.025, 0.975])
print("95% Confidence Interval:", confidence_interval)


# In[56]:


from sklearn.linear_model import Lasso
diabetes_df = pd.read_csv('diabetes.csv', index_col = 0)
diabetes_df = diabetes_df[diabetes_df['bmi'] != 0]
diabetes_df = diabetes_df[diabetes_df['glucose'] != 0]
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scores = []
for alpha in [0.01,1.0,10.0, 20.0, 50.0]:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    lasso_pred = lasso.predict(X_test)
    scores.append(lasso.score(X_test, y_test))
print(scores)


# In[57]:


diabetes_df = pd.read_csv('diabetes.csv', index_col = 0)
diabetes_df = diabetes_df[diabetes_df['bmi'] != 0]
diabetes_df = diabetes_df[diabetes_df['glucose'] != 0]
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
names = diabetes_df.drop('glucose', axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X,y).coef_
plt.bar(names, lasso_coef)
plt.xticks(rotation=45)
plt.show()


# In[67]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

sales_df = pd.read_csv('sales_df.csv')

X = sales_df.drop(columns=['sales']) 
y = sales_df['sales']               

sales_columns = X.columns

lasso = Lasso(alpha=0.3)

lasso.fit(X, y)

lasso_coef = lasso.coef_

plt.figure(figsize=(10, 6))
plt.bar(sales_columns, lasso_coef)
plt.title("Lasso Coefficients for Feature Importance")
plt.xticks(rotation=90)
plt.show()


# In[69]:





# In[73]:


from sklearn.metrics import classification_report, confusion_matrix
knn = KNeighborsClassifier(n_neighbors = 7)
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.4, random_state = 42)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# In[72]:


music_df = pd.read_csv('music.csv', index_col = 0)
music_dummies = pd.get_dummies(music_df['genre'], drop_first=True)
#music_dummies.head()
music_dummies = pd.concat([music_df, music_dummies], axis = 1)
music_dummies = music_dummies.drop('genre', axis=1)
#music_dummies.head()
print(music_dummies.columns)
#from sklearn.model_selection import cross_val_score, KFold
#from sklearn.linear_model import LinearRegression
X = music_dummies.drop('popularity', axis=1).values
y = music_dummies['popularity'].values
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,
random_state=42)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
linreg = LinearRegression()
linreg_cv = cross_val_score(linreg, X_train, y_train, cv=kf,
scoring='neg_mean_squared_error')
linreg_cv2 = cross_val_score(linreg, X_train, y_train, cv=kf)
print(np.sqrt(-linreg_cv))
print(linreg_cv2)


# In[74]:


#code for SimpleImputer example

from sklearn.impute import SimpleImputer

 

music_df = pd.read_csv('music_unclean.csv', index_col = 0)
print(music_df.columns)
print(music_df.isna().sum().sort_values())
music_df = music_df.dropna(subset=['genre','popularity','loudness','liveness','tempo'])
music_df['genre'] = np.where(music_df['genre'] == 'Rock', 1,0)
print(music_df.isna().sum().sort_values())

 

X_cat = music_df['genre'].values.reshape(-1,1)
X_num = music_df.drop(['genre','popularity'], axis=1).values
y = music_df['popularity'].values

 

X_train_cat, X_test_cat, y_train, y_test = train_test_split(X_cat, y, test_size=0.3,
random_state = 12)
X_train_num, X_test_num, y_train, y_test = train_test_split(X_num, y, test_size=0.3,
random_state = 12)

 

imp_cat = SimpleImputer(strategy='most_frequent')
X_train_cat = imp_cat.fit_transform(X_train_cat)
X_test_cat = imp_cat.transform(X_test_cat)

 

imp_num = SimpleImputer()
X_train_num = imp_num.fit_transform(X_train_num)
X_test_num = imp_num.transform(X_test_num)

 

X_train = np.append(X_train_num, X_train_cat, axis=1)
X_test = np.append(X_test_num, X_test_cat, axis=1)

 

columns = ['acousticness', 'danceability', 'duration_ms', 'energy',
'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
'valence', 'genre']
check = pd.DataFrame(X_train, columns = columns)
print(check.isna().sum().sort_values())

 

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(knn.score(X_test, y_test))


# In[76]:


from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
music_df = pd.read_csv('music_unclean.csv', index_col =
0)
music_df = music_df.dropna(subset=['genre',
'popularity','loudness','liveness','tempo'])
music_df['genre'] = np.where(music_df['genre'] ==
'Rock', 1, 0)
X = music_df.drop('genre', axis = 1).values
y = music_df['genre'].values
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
steps = [('imputation', SimpleImputer()),
('Log_reg', LogisticRegression())]
pipeline = Pipeline(steps)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(pipeline.score(X_test,y_test))


# In[78]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

music_df = pd.read_csv('music_unclean.csv')

missing_values = music_df.isnull().sum().sort_values(ascending=True)
print("Missing Values per Column:")
print(missing_values)

music_df = music_df.dropna(thresh=len(music_df) - 50, axis=1)

music_df["genre"] = (music_df["genre"] == "Rock").astype(int)

X = music_df.drop(columns=["genre"])
y = music_df["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

imputer = SimpleImputer(strategy="mean")

knn = KNeighborsClassifier(n_neighbors=3)

steps = [("imputer", imputer), ("knn", knn)]

pipeline = Pipeline(steps)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)


# In[79]:


#Without using pipeline

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

music_df = pd.read_csv('music_unclean.csv')

missing_values = music_df.isnull().sum().sort_values(ascending=True)
print("Missing Values per Column:")
print(missing_values)
music_df = music_df.dropna(thresh=len(music_df) - 50, axis=1)

music_df["genre"] = (music_df["genre"] == "Rock").astype(int)

X = music_df.drop(columns=["genre"])
y = music_df["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

imputer = SimpleImputer(strategy="mean")

X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train_imputed, y_train)

y_pred = knn.predict(X_test_imputed)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)


# In[ ]:




