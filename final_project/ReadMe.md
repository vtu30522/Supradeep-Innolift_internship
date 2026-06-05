# Credit Card Fraud Detection Project
## Project Overview
This project is about detecting fraudulent credit card transactions using Machine Learning. The model learns from past transaction data and predicts whether a transaction is normal or fraud.
---
## Dataset
I have used the Kaggle Credit Card Fraud Detection dataset.
Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
The dataset contains transactions made by credit cards in September 2013. It has features like Time, Amount, and other transformed variables (V1 to V28), along with the target column Class.
---
## Objective
The main goal of this project is to build a machine learning model that can identify fraudulent transactions accurately.
---
## Steps Performed

### 1. Data Loading
- Loaded the dataset using pandas
- Checked shape, head, and data types

### 2. Data Cleaning
- Checked for missing values
- Verified dataset has no null values
- Removed duplicates (if any)

### 3. Exploratory Data Analysis (EDA)
- Analyzed fraud vs non-fraud transactions
- Studied correlation between features
- Created visualizations

### 4. Data Visualization
- Fraud distribution graph
- Top features affecting fraud
- Correlation heatmap

### 5. Model Building
- Used Random Forest Classifier
- Split data into 80% training and 20% testing
- Trained the model on dataset

### 6. Model Saving
- Saved trained model using pickle as model.pkl

### 7. Prediction
- Loaded saved model
- Tested multiple transaction cases
- Predicted whether transaction is fraud or normal

---

## Model Used
Random Forest Classifier
---
## Accuracy
The model gives high accuracy (around 99%) because the dataset is well structured and clean.
---
## Project Files

- train_model.py → model training
- predict.py → predictions on new data
- visualization.py → charts and graphs
- model.pkl → saved trained model
- creditcard.csv → dataset
- PNG files → visualizations

---

## How to Run

Install requirements:
pip install pandas numpy matplotlib scikit-learn

Train model:
python train_model.py

Run predictions:
python predict.py

Generate visualizations:
python visualization.py


---

## What I Learned
- Basics of Machine Learning
- Data preprocessing and analysis
- Model training and evaluation
- How to save and load ML models
- Visualization using matplotlib

---

## Conclusion
This project helped me understand how machine learning can be used in real-world applications like fraud detection in banking systems.