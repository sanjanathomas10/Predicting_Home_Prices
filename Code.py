#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[6]:


data = pd.read_csv('home_dataset.csv')
 
house_sizes = data ['HouseSize'].values
house_prices = data['HousePrice'].values


# In[7]:


# Visualizing data
plt.scatter(house_sizes, house_prices, marker ='o', color ='blue')
plt.title('House Prices vs. House Size')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price ($)')
plt.show()


# In[8]:


# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(house_sizes, house_prices, test_size=0.2, random_state=42)


# In[9]:


x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

# Creating and training model
model = LinearRegression()
model.fit(x_train, y_train)


# In[10]:


# Predicting prices for the test set
predictions = model.predict(x_test)

# Visualizing predictions
plt.scatter(x_test, y_test, marker='o', color='blue', label='Actual Prices')
plt.plot(x_test, predictions, color='red', linewidth=2, label='Predicted Prices')
plt.title('Dumbo Property Price Prediction with Linear Regression')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price (millions $)')
plt.legend()
plt.show()


# In[11]:


from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Calculating R², MAE, and RMSE
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("Model Evaluation Metrics:")
print(f"R² Score: {r2:.2f}")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")


# In[ ]:




