# AI-Powered Enterprise Data Leakage Prevention System

## Overview

AI-Powered Enterprise Data Leakage Prevention System is a cybersecurity prototype project designed to detect, analyze, and prevent sensitive data leakage.

The system monitors uploaded documents/messages, identifies confidential information, calculates risk levels, prevents unauthorized data transfer, and provides security monitoring through employee and admin dashboards.

---

## Features

## Employee Module

- Secure Login Authentication
- Role-Based Access Control
- Upload and Scan Documents
- Sensitive Data Detection
- Risk Level Classification
- Scan History Management
- Employee Dashboard
- Recent Activity Monitoring

## Admin Module

- Admin Authentication
- Employee Monitoring
- Total Scan Statistics
- Blocked Attempt Monitoring
- Risk Analytics
- Incident Tracking
- System Logs
- Security Dashboard

---

## System Architecture

```
User
 |
 | Login Authentication
 |
Employee Dashboard
 |
 | Upload Document / Message
 |
Data Scanner
 |
Sensitive Data Detection
 |
AI Risk Analysis
 |
Risk Decision
 |
 |-------- Allow
 |
 |-------- Block
 |
Incident Logging
 |
Admin Dashboard
```

---

## Technology Stack

### Frontend

- Python
- Streamlit
- Pandas

### Backend

- FastAPI
- SQLAlchemy
- Python

### Database

- PostgreSQL

### Document Processing

- pdfplumber
- python-docx

### Security

- Password Authentication
- Role-Based Access Control
- Secure Data Validation

---

## Project Structure

```
data_leakage

├── backend
│   └── FastAPI Application
│       ├── app
│       │   ├── routes
│       │   ├── models
│       │   ├── schemas
│       │   └── services
│
├── frontend
│   └── Streamlit Application
│       ├── pages
│       │   ├── login.py
│       │   ├── employee_dashboard.py
│       │   ├── admin_dashboard.py
│       │   ├── history.py
│       │   └── module1.py
│
└── README.md
```

---

## How to Run

### Backend

Navigate to backend folder:

```
cd backend
```

Install dependencies:

```
pip install -r requirements.txt
```

Run FastAPI:

```
uvicorn app.main:app --reload
```

Backend runs:

```
http://127.0.0.1:8000
```

---

### Frontend

Navigate to frontend folder:

```
cd frontend
```

Run Streamlit:

```
streamlit run app.py
```

---

## Project Type

Cybersecurity Prototype Project

## Domain

Artificial Intelligence + Data Security + Data Loss Prevention (DLP)

---

## Future Enhancements

- Real-time email monitoring
- Machine Learning based risk prediction
- Cloud deployment
- Advanced user behavior analytics
- Enterprise security integrations