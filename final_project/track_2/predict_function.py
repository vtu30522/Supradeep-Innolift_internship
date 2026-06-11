import pandas as pd
import joblib


def predict(inputs: dict) -> dict:

    try:

        model = joblib.load(
            r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\final_model.pkl"
        )

        input_df = pd.DataFrame([inputs])

        prediction = model.predict(input_df)[0]

        probabilities = model.predict_proba(input_df)[0]

        confidence = max(probabilities) * 100

        if prediction == 1:

            return {
                "Prediction": "Fraud Transaction",
                "Confidence": f"{confidence:.2f}%",
                "Risk Level": "High Risk",
                "Top Features": "V17, V14, V12"
            }

        else:

            return {
                "Prediction": "Normal Transaction",
                "Confidence": f"{confidence:.2f}%",
                "Risk Level": "Low Risk",
                "Top Features": "V17, V14, V12"
            }

    except Exception as e:

        return {
            "Prediction": "Error",
            "Confidence": "N/A",
            "Risk Level": "N/A",
            "Top Features": str(e)
        }


# TEST THE FUNCTION

sample_df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\sample_transaction.csv"
)

sample = sample_df.iloc[0].to_dict()

result = predict(sample)

result_df = pd.DataFrame([result])

print("\nPREDICTION RESULT\n")
print(result_df.to_string(index=False))