import pandas as pd
from predict_function import predict

print("\nTASK 3 - 10 TEST CASES\n")

transactions = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\sample_transaction.csv"
)

results = []

for i in range(len(transactions)):

    transaction = transactions.iloc[i].to_dict()

    try:

        result = predict(transaction)

        results.append({
            "Case": i + 1,
            "Prediction": result["Prediction"],
            "Confidence": result["Confidence"],
            "Status": "PASS"
        })

    except Exception:

        results.append({
            "Case": i + 1,
            "Prediction": "Error",
            "Confidence": "N/A",
            "Status": "ERROR"
        })

results_df = pd.DataFrame(results)

print(results_df.to_string(index=False))