# Predicting Home Prices
*Python and Linear Regression*

### 📑 Background 📑
---
**Real estate pricing** is a crucial economic and social factor, influencing housing affordability, urban planning, and investment decisions. Accurately estimating property prices helps both buyers and sellers make informed choices, while *enabling businesses and policymakers to track market trends.*
This project demonstrates how *machine learning techniques*, specifically *linear regression*, can be applied to predict house prices based on property size. 

Insights and outcomes are provided on the following key areas:

**Data Exploration & Visualization:**
Analysis of the relationship between house size and price through scatter plots, highlighting linear trends.

**Model Development:**
Implementation of a linear regression model using Scikit-learn, trained on historical house size and pricing data.

**Model Validation:**
Application of a train-test split to evaluate predictive accuracy, ensuring the model can generalize to unseen data.

**Prediction & Visualization:**
Comparison of actual vs. predicted prices using regression line plots for clear interpretability and evaluation of model based on key metrics.

---
### 🗂️ Data Structure and Sources 🗂️
---
The dataset used for this project was publicly available on 
**[Zillow](https://www.zillow.com/).** and can be downloaded [here](https://drive.google.com/file/d/1cNtzy7IwR753aXvpaYQRuEoxMfUNnYHl/view?usp=sharing)

The dataset had two columns: 
<img width="158" height="29" alt="Screenshot 2025-09-04 at 6 32 15 PM" src="https://github.com/user-attachments/assets/b727de51-1756-4a25-a7b1-118a54cfbd7f" />

---
### 📊 Executive Summary 📊
---

This project applies linear regression to predict house prices based on house size, using a dataset of recently sold properties. The model reveals a strong positive relationship between house size and price, demonstrating the usefulness of predictive analytics in real-estate markets.

Below is the workflow and findings, supported by visualizations of both the raw data and the model predictions.

**Data Visualization**

<img width="276" height="222" alt="Screenshot 2025-09-04 at 6 56 38 PM" src="https://github.com/user-attachments/assets/626888e6-37ac-4c19-b0d8-503aa684f6c6" />

This visualization highlights the underlying trend between house size and price, confirming a generally linear relationship suitable for regression analysis.

**Model Fit & Predictions**


<img width="285" height="220" alt="Screenshot 2025-09-04 at 6 57 14 PM" src="https://github.com/user-attachments/assets/ed95ce20-d08c-468a-b745-b1a1333abc8c" />


The model’s predictions (red regression line) closely follow the actual observed values (blue points), showing a good fit and capturing most of the variation in the data.


**Model Evaluation Metrics**

Using metrics such as the *R² Score, Mean Absolute Error (MAE),* and *Root Mean Squared Error (RMSE)*, we can evaluate that

90% of the variation in house prices is explained by house size.
On average, predictions deviate from actual prices by ~$143K.
Larger errors exist, but remain within a reasonable range for this dataset.

**Overall, the model demonstrates strong predictive power, confirming that house size is a significant driver of price. This predictive framework can be extended to incorporate more features (e.g., location, number of rooms, or amenities) to improve accuracy and provide actionable insights for pricing strategy in real-estate markets.**
