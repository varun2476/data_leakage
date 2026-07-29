import re

# =========================
# KEYWORDS
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
    "marksheet",
    "hall ticket",
    "admit card",
    "10th",
    "12th",
    "intermediate",
    "diploma",
    "degree"
]

# =========================
# REGEX PATTERNS
# =========================
PATTERNS = {

    "Aadhaar Number": r"\b(?:\d[\s-]*){12}\b",

    "PAN Number": r"\b[A-Za-z]{5}[0-9]{4}[A-Za-z]\b",

    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",

    "Phone Number": r"\b[6-9]\d{9}\b",

    "Credit Card": r"\b(?:\d[ -]*?){13,16}\b",

    "IFSC Code": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

    "OTP": r"\b\d{6}\b",

    "API Key": r"(api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{10,})",

    "JWT Token": r"eyJ[a-zA-Z0-9_\-\.]+",

    "Salary": r"(₹\s?\d+|\b\d+\s?(rs|rupees)\b)"
}

def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email)
# =========================
# MAIN FUNCTION
# =========================
def analyze_text(text):

    print("INPUT TEXT:")
    print(text)

    detections = []

    # REGEX DETECTION
    for item_type, pattern in PATTERNS.items():

        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:

            if isinstance(match, tuple):
                value = match[0]
            else:
                value = match

            detections.append({
                "Type": item_type,
                "Value": value
            })

    # Remove duplicates
    unique = []
    seen = set()

    for item in detections:

        key = (item["Type"], item["Value"])

        if key not in seen:
            seen.add(key)
            unique.append(item)

    detections = unique

    # Risk
    if len(detections) == 0:

        return {
            "detected": False,
            "risk": "SAFE",
            "message": "No sensitive information found.",
            "detections": []
        }

    elif len(detections) == 1:

        return {
            "detected": True,
            "risk": "HIGH",
            "message": "Sensitive information detected.",
            "detections": detections
        }

    else:

        return {
            "detected": True,
            "risk": "CRITICAL",
            "message": f"{len(detections)} sensitive items detected.",
            "detections": detections
        }