import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("../dataset/confidential_dataset.csv")

# Input (text)
X = df["text"]

# Output (label)
y = df["label"]

# Convert text into numerical features
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train ML model
model = LogisticRegression()

model.fit(X_vectorized, y)

# Save model
joblib.dump(model, "model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")
print("model.pkl created")
print("vectorizer.pkl created")