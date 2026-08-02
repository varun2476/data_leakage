from app.services.ml_service import analyze_document


text = """
Employee payroll details
Salary information
Bank account details
"""


result = analyze_document(text)

print(result)