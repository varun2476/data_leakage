import pandas as pd
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# =========================
# Dataset Path
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
)


dataset_path = os.path.join(
    BASE_DIR,
    "dataset",
    "confidential_dataset.csv"
)


print("Dataset Location:")
print(dataset_path)


# =========================
# Load Dataset
# =========================

df = pd.read_csv(dataset_path)


print(df.head())
print(df.columns)


# =========================
# Input and Output
# =========================

X = df["text"]

y = df["label"]


# =========================
# Text Conversion
# =========================

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# =========================
# Train Model
# =========================

model = LogisticRegression()

model.fit(
    X_vectorized,
    y
)


# =========================
# Save Model
# =========================

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model.pkl"
)


VECTOR_PATH = os.path.join(
    os.path.dirname(__file__),
    "vectorizer.pkl"
)


joblib.dump(
    model,
    MODEL_PATH
)


joblib.dump(
    vectorizer,
    VECTOR_PATH
)


print("========================")
print("Model trained successfully!")
print("model.pkl created")
print("vectorizer.pkl created")
print("========================")