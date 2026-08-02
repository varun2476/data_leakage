from app.ml.ml_classifier import predict_document


def analyze_document(text):

    label, confidence = predict_document(text)

    result = {
        "classification": label,
        "confidence": confidence
    }

    return result