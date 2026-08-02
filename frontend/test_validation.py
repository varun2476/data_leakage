from validate import analyze_text


text = """
Employee salary report for July 2026

Employee payroll details

Bank account information

PAN Number: ABCDE1234F
"""


result = analyze_text(text)


print("====================")
print("FINAL RESULT")
print("====================")

print(result)