import joblib

model = joblib.load(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\best_model.pkl"
)

joblib.dump(
    model,
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\track_2\final_model.pkl"
)

print("final_model.pkl created successfully")