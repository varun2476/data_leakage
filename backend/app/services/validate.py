import re

from app.ml.ml_classifier import predict_document


# =========================
# SENSITIVE KEYWORDS
# =========================

SENSITIVE_KEYWORDS = [
    "bank account",
    "account number",
    "ifsc",
    "upi",
    "password",
    "secret",
    "api key",
    "apikey",
    "token",
    "cvv",
    "otp",
    "salary",
    "credit card",
    "debit card",
    "passport",
    "aadhaar",
    "pan",
    "ration card",
    
]


# =========================
# REGEX PATTERNS
# =========================

PATTERNS = {

    "Aadhaar Number":
        r"\b(?:\d[\s-]*){12}\b",

    "PAN Number":
        r"\b[A-Za-z]{5}[0-9]{4}[A-Za-z]\b",

    "Email":
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",

    "Phone Number":
        r"\b[6-9]\d{9}\b",

    "Credit Card":
        r"\b(?:\d[ -]*?){13,16}\b",

    "IFSC Code":
        r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

    "OTP":
        r"\b\d{6}\b",

    "API Key":
        r"(api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{10,})",

    "JWT Token":
        r"eyJ[a-zA-Z0-9_\-\.]+",

    "Salary":
        r"(₹\s?\d+|\b\d+\s?(rs|rupees)\b)"
}



# =========================
# EMAIL VALIDATION
# =========================

def is_valid_email(email):

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email)



# =========================
# MAIN ANALYSIS FUNCTION
# =========================

def analyze_text(text):

    print("======================")
    print("INPUT TEXT")
    print(text)
    print("======================")


    detections = []


    # =========================
    # REGEX SCANNING
    # =========================

    for item_type, pattern in PATTERNS.items():

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE
        )


        for match in matches:


            if isinstance(match, tuple):

                value = match[0]

            else:

                value = match


            detections.append({

                "Type": item_type,

                "Value": value

            })



    # =========================
    # KEYWORD SCANNING
    # =========================

    lower_text = text.lower()


    for keyword in SENSITIVE_KEYWORDS:


        if keyword in lower_text:


            detections.append({

                "Type": "Sensitive Keyword",

                "Value": keyword

            })



    # =========================
    # REMOVE DUPLICATES
    # =========================

    unique = []

    seen = set()


    for item in detections:


        key = (

            item["Type"],

            item["Value"]

        )


        if key not in seen:

            seen.add(key)

            unique.append(item)



    detections = unique



    # =========================
    # ML CLASSIFICATION
    # =========================

    try:


        ml_label, ml_confidence = predict_document(text)


    except Exception as e:


        print("ML Error:", e)


        ml_label = "Unknown"

        ml_confidence = 0

# =========================
# FINAL RISK ENGINE
# =========================

    sensitive_count = len(detections)

    if sensitive_count == 0:
            risk = "SAFE"

    elif sensitive_count == 1:
            risk = "LOW"

    elif sensitive_count == 2:
            risk = "MEDIUM"

    elif sensitive_count == 3:
            risk = "HIGH"

    else:
            risk = "CRITICAL"


# Optional: Upgrade risk based on ML predictio
    if ml_label == "Confidential" and ml_confidence >= 85:

        if risk == "LOW":
            risk = "MEDIUM"

        elif risk == "MEDIUM":
            risk = "MEDIUM"

        elif risk == "HIGH":
            risk = "CRITICAL"



    # =========================
    # FINAL RESPONSE
    # =========================


    return {


        "detected":

            sensitive_count > 0,


        "risk":

            risk,


        "message":

            "Analysis completed successfully",


        "detections":

            detections,


        "ml_prediction":

            ml_label,


        "ml_confidence": float(ml_confidence),


        "total_sensitive_items":

            sensitive_count

    }