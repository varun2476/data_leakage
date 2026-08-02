import pandas as pd
import random


confidential_templates = [
    "Employee salary report for {month} {year}",
    "Employee payroll details and bonus information",
    "Customer credit card information and transaction details",
    "Company bank account information",
    "Internal financial statement of company",
    "Confidential merger discussion document",
    "Employee personal information record",
    "Employee Aadhaar number and PAN details",
    "Customer payment information",
    "Private employee performance report",
    "Company secret business strategy document",
    "Database password and API key information",
    "Vendor payment details",
    "Internal HR salary analysis",
    "Confidential customer database",
    "Employee attendance and salary report",
    "Company revenue report",
    "Private client contract agreement",
    "Insurance customer information",
    "Employee tax details"
]


public_templates = [
    "Company holiday announcement",
    "Office sports event notice",
    "Public recruitment advertisement",
    "Marketing brochure",
    "Company newsletter",
    "Public festival celebration announcement",
    "Company website information",
    "Employee training schedule",
    "Public product advertisement",
    "Office event invitation",
    "Company social media announcement",
    "Public internship announcement",
    "General company information",
    "Annual public meeting announcement",
    "Customer support contact information"
]


months = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]


rows = []


# Create 600 confidential rows

for i in range(600):

    text = random.choice(confidential_templates)

    text = text.format(
        month=random.choice(months),
        year=random.randint(2024,2026)
    )

    rows.append(
        {
            "text": text,
            "label": "Confidential"
        }
    )


# Create 600 public rows

for i in range(600):

    text = random.choice(public_templates)

    rows.append(
        {
            "text": text,
            "label": "Public"
        }
    )


# Shuffle dataset

random.shuffle(rows)


df = pd.DataFrame(rows)


df.to_csv(
    "confidential_dataset.csv",
    index=False
)


print("Dataset created successfully")
print("Total rows:", len(df))