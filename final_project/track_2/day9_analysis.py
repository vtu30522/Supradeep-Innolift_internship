import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

from imblearn.over_sampling import SMOTE

df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\creditcard.csv"
)

print("Dataset Loaded Successfully")

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data Split Completed")

model_path = r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\best_model.pkl"

model = joblib.load(model_path)

print("Model Loaded Successfully")

print("\nTASK 1 - FEATURE IMPORTANCE")

def feature_importance_analysis():

    importance_df = pd.DataFrame({
        "Feature": X_train.columns,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nTop 10 Important Features")
    print(importance_df.head(10))

    plt.figure(figsize=(10,8))

    plt.barh(
        importance_df["Feature"][:15],
        importance_df["Importance"][:15]
    )

    plt.title("Feature Importance")
    plt.xlabel("Importance Score")

    plt.tight_layout()

    plt.savefig(
        r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\feature_importance.png"
    )

    plt.show()

feature_importance_analysis()

print("\nTASK 2 - CLASS IMBALANCE")

print("\nBefore SMOTE")
print(y_train.value_counts())

smote = SMOTE(
    random_state=42
)

X_train_balanced, y_train_balanced = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter SMOTE")
print(
    pd.Series(y_train_balanced).value_counts()
)

print("\nTASK 3 - MODEL EXPLAINABILITY")

feature_scores = list(
    zip(
        X_train.columns,
        model.feature_importances_
    )
)

feature_scores.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 3 Important Features")

for i, (name, score) in enumerate(
    feature_scores[:3],
    1
):
    print(
        f"{i}. {name} = {score:.4f}"
    )

print("\nTASK 4 - OUTPUT ENRICHMENT")

def enrich_prediction(prediction, probability):

    confidence = max(probability) * 100

    if prediction == 1:
        return {
            "Prediction": "Fraud Transaction",
            "Confidence": f"{confidence:.2f}%",
            "Risk Level": "High Risk",
            "Action": "Block Transaction",
            "Alert": "Notify Security Team"
        }

    else:
        return {
            "Prediction": "Normal Transaction",
            "Confidence": f"{confidence:.2f}%",
            "Risk Level": "Low Risk",
            "Action": "Approve Transaction",
            "Alert": "No Action Required"
        }


def check_transaction():

    transaction_df = pd.read_csv(
        r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\sample_transaction.csv"
    )

    predictions = model.predict(transaction_df)

    probabilities = model.predict_proba(transaction_df)

    for i in range(len(transaction_df)):

        result = enrich_prediction(
            predictions[i],
            probabilities[i]
        )

        print("\n" + "=" * 50)
        print(f"Transaction {i+1}")

        for key, value in result.items():
            print(f"{key}: {value}")


check_transaction()

print("\nTASK 5 - FULL PIPELINE TESTING")

transaction_df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\sample_transaction.csv"
)

predictions = model.predict(transaction_df)

probabilities = model.predict_proba(transaction_df)

results = []

for i in range(len(transaction_df)):

    confidence = max(probabilities[i]) * 100

    prediction_label = (
        "Fraud Transaction"
        if predictions[i] == 1
        else "Normal Transaction"
    )

    results.append([
        i + 1,
        prediction_label,
        f"{confidence:.2f}%"
    ])

results_df = pd.DataFrame(
    results,
    columns=[
        "Transaction No",
        "Prediction",
        "Confidence"
    ]
)

print("\nFINAL TEST RESULTS")
print(results_df)