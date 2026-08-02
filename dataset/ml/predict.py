import joblib

print("Loading model...")

# Load trained model
model = joblib.load("model.pkl")

# Load vectorizer
vectorizer = joblib.load("vectorizer.pkl")

print("Model loaded successfully!")

# Test document
text = [
    "Employee salary report for July 2026"
]

# Convert text into numerical features
text_vector = vectorizer.transform(text)

# Predict
prediction = model.predict(text_vector)

# Get confidence score
probability = model.predict_proba(text_vector)

print("\n========== RESULT ==========")
print("Input Text:", text[0])
print("Prediction:", prediction[0])
print("Confidence:", round(max(probability[0]) * 100, 2), "%")