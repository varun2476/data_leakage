from app.ml.ml_classifier import predict_document
from app.services.validate import analyze_text


def scan_document(text):

    # Regex analysis
    result = analyze_text(text)


    # ML prediction
    ml_label, confidence = predict_document(text)


    result["ml_prediction"] = ml_label
    result["ml_confidence"] = confidence


    # Final risk decision

    

    return result