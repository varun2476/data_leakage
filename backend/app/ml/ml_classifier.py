import joblib
import os


# Current ML folder path

BASE_DIR = os.path.dirname(__file__)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)


VECTOR_PATH = os.path.join(
    BASE_DIR,
    "vectorizer.pkl"
)


# Load model

model = joblib.load(MODEL_PATH)


# Load vectorizer

vectorizer = joblib.load(VECTOR_PATH)



def predict_document(text):

    # Convert text

    vector = vectorizer.transform([text])


    # Prediction

    prediction = model.predict(vector)[0]


    # Probability

    probability = model.predict_proba(vector)

    confidence = max(probability[0]) * 100


    return prediction, round(confidence,2)