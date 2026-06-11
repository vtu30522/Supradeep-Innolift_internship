import joblib
import pandas as pd

model = joblib.load(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\final_model.pkl"
)

print("Model Loaded Successfully")

sample_data = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\sample_transaction.csv"
)

prediction = model.predict(sample_data)

print("Predictions:")
print(prediction)