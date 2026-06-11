## Model Summary Card

### Project

Credit Card Fraud Detection System · Finance / Cyber Security

### Algorithm

Random Forest Classifier (Tuned and Optimized)

### Dataset

Credit Card Fraud Detection Dataset · 284,807 Transactions · 30 Features

### Final Performance

| Metric              | Score  |
| ------------------- | ------ |
| Accuracy            | 99.96% |
| Precision           | 0.95   |
| Recall              | 0.84   |
| F1-Score (Weighted) | 0.99   |

### Input Features (in this exact order)

| Column | Type  | Example Value |
| ------ | ----- | ------------- |
| Time   | float | 1000          |
| V1     | float | -2.312227     |
| V2     | float | 1.951992      |
| V3     | float | -1.609851     |
| V4     | float | 3.997906      |
| V5     | float | -0.522188     |
| V6     | float | -1.426545     |
| V7     | float | -2.537387     |
| V8     | float | 1.391657      |
| V9     | float | -2.770089     |
| V10    | float | -2.772272     |
| V11    | float | 3.202033      |
| V12    | float | -2.899907     |
| V13    | float | -0.595222     |
| V14    | float | -4.289254     |
| V15    | float | 0.389724      |
| V16    | float | -1.140747     |
| V17    | float | -2.830056     |
| V18    | float | -0.016822     |
| V19    | float | 0.416956      |
| V20    | float | 0.126911      |
| V21    | float | 0.517232      |
| V22    | float | -0.035049     |
| V23    | float | -0.465211     |
| V24    | float | 0.320198      |
| V25    | float | 0.044519      |
| V26    | float | 0.177840      |
| V27    | float | 0.261145      |
| V28    | float | -0.143276     |
| Amount | float | 0.00          |

### Required .pkl Files

| File            | Contents                          |
| --------------- | --------------------------------- |
| final_model.pkl | Final Trained Random Forest Model |

### Sample Input

```python
{
    'Time':1000,
    'V1':-2.312227,
    'V2':1.951992,
    'V3':-1.609851,
    'V4':3.997906,
    'V5':-0.522188,
    'V6':-1.426545,
    'V7':-2.537387,
    'V8':1.391657,
    'V9':-2.770089,
    'V10':-2.772272,
    'V11':3.202033,
    'V12':-2.899907,
    'V13':-0.595222,
    'V14':-4.289254,
    'V15':0.389724,
    'V16':-1.140747,
    'V17':-2.830056,
    'V18':-0.016822,
    'V19':0.416956,
    'V20':0.126911,
    'V21':0.517232,
    'V22':-0.035049,
    'V23':-0.465211,
    'V24':0.320198,
    'V25':0.044519,
    'V26':0.177840,
    'V27':0.261145,
    'V28':-0.143276,
    'Amount':0.00
}
```

### Sample Output

```python
{
    'Prediction': 'Fraud Transaction',
    'Confidence': '90.00%',
    'Risk Level': 'High Risk',
    'Top Features': 'V17, V14, V12'
}
```

### Explainability Features

Top 3 Important Features Identified:

1. V17
2. V14
3. V12

These features contribute the most to fraud prediction according to the Random Forest Feature Importance analysis.

### How to Use

```python
from predict_function import predict

result = predict(transaction_input)

print(result)
```

### Project Outputs

* Feature Importance Analysis
* Class Imbalance Handling using SMOTE
* Model Explainability using Feature Importance
* Output Enrichment with Risk Level and Actions
* Full Pipeline Testing with 10 Transactions
* Final Random Forest Model Saved as final_model.pkl
