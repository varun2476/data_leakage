import joblib

print("Loading model...")

# Load the trained model
model = joblib.load("model.pkl")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("vectorizer.pkl")

print("Model loaded successfully!")

# Test input
text = ["Employee salary report for July 2026"]

# Convert text to TF-IDF features
text_vector = vectorizer.transform(text)

# Predict
prediction = model.predict(text_vector)

# Confidence score
probability = model.predict_proba(text_vector)

print("\n===== Prediction Result =====")
print("Input:", text[0])
print("Prediction:", prediction[0])
print("Confidence:", round(max(probability[0]) * 100, 2), "%")