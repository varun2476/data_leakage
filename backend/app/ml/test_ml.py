from app.ml.ml_classifier import predict_document


text = """

Employee salary report July 2026

Employee payroll details

Bank account information

"""


label, confidence = predict_document(text)


print("Prediction:", label)
print("Confidence:", confidence)