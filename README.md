# 🔐 AI-Powered Enterprise Data Leakage Prevention System


# 🚀 Overview

The **AI-Powered Enterprise Data Leakage Prevention (DLP) System** is an intelligent cybersecurity platform designed to detect, analyze, and prevent unauthorized leakage of confidential enterprise information.

The system works as a security layer between employees and organizational data. Before sharing files or sensitive information, employees can upload documents and messages for automated security scanning.

The platform extracts content, identifies sensitive information, performs AI-based risk analysis, generates security decisions, maintains audit records, and sends automated alerts to administrators during critical security events.


The system provides two major security portals:

---

# 👨‍💻 Employee Security Portal

The Employee Security Portal allows employees to securely access the system, scan files before sharing, and monitor their security activities.

Employees can:

- Register an account
- Login securely
- Upload documents for scanning
- Detect sensitive information
- View risk analysis results
- Receive security warnings
- View scanning history
- Manage profile information


---

# 👑 Admin Security Dashboard

The Admin Security Dashboard provides complete organizational security monitoring.

Administrators can:

- Monitor registered employees
- View employee departments and roles
- Analyze security statistics
- Monitor scanning activities
- View blocked data transfer attempts
- Manage security incidents
- Receive email alerts
- Analyze risk levels
- Review security logs


---

# 🎯 Project Objectives


The main objectives of this project are:

- Prevent confidential data leakage
- Detect sensitive information automatically
- Protect enterprise documents
- Analyze security risks before data sharing
- Block unauthorized transfers
- Maintain security audit trails
- Provide administrator monitoring
- Improve organizational data protection



# 🔄 Complete System Workflow


```
                    USER

                     |

                     |

              Registration

                     |

                     |

              Secure Login

                     |

                     |

              Role Verification

                     |

        ----------------------------

        |                          |

     USER                       ADMIN

        |                          |

Employee Dashboard          Admin Dashboard

        |                          |

Upload File                 View Employees

        |                          |

Text Extraction              View Activities

        |                          |

Sensitive Data Detection     View Incidents

        |                          |

Risk Analysis                View Alerts

        |                          |

Decision Engine              Risk Analytics


        |

        |

----------------------------------

|                                |

LOW / MEDIUM                 HIGH / CRITICAL

|                                |

Allow Sharing                 Block Transfer

|                                |

Save History                  Create Incident

                                 |

                                 |

                         Send Admin Alert Email

```



# 👨‍💻 Employee Module Workflow


## 1. Employee Registration


Employees create accounts by providing:


- Name
- Email
- Password
- Department
- Role


Registration Flow:


```
Employee Registration

        |

        |

Input Validation

        |

        |

Store Employee Data

        |

        |

Login Access

```


---

# 2. Employee Login


The authentication system verifies:


- Email
- Password
- Role


Supported role:


```
USER

 |

Employee Security Portal


ADMIN

 |

Admin Security Dashboard

```



After successful login:

```
USER

      |

Employee Dashboard


ADMIN

      |

Admin Dashboard

```



---

# 3. Employee Dashboard Features


The employee dashboard provides:


## Document Security Scanner

Employees can upload:


- PDF files
- Word documents
- Text files


Processing:


```
Upload Document

        |

        |

Extract Text

        |

        |

Sensitive Data Detection

        |

        |

Risk Analysis

        |

        |

Security Decision

```



---

# 🔍 Sensitive Data Detection Module


The scanner detects:


## Personal Sensitive Information


- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers


## Enterprise Confidential Information


- Financial information
- Internal documents
- Confidential keywords
- Restricted information


Detection methods:


- Regular Expression Validation
- Rule-Based Detection
- AI Content Analysis



Example:


```
Input:

Customer Aadhaar:
1234 5678 9012


Detection:

Sensitive Data Found


Risk:

HIGH

```



---

# 🤖 AI Risk Analysis Engine


The system classifies scanned content into security levels.


```
LOW RISK

No confidential information

Action:

Allow Sharing



MEDIUM RISK

Sensitive information detected

Action:

Warning Alert



HIGH RISK

Confidential information detected

Action:

Block Sharing

Create Incident



CRITICAL RISK

Severe security violation

Action:

Immediate Alert

Admin Notification

```



---

# ⚙️ Security Decision Engine


After analysis, the system automatically decides:


```
Scan Result

       |

       |

Risk Calculation

       |

       |

-------------------------

|                       |

SAFE                  HIGH RISK

|                       |

Allow                Block

|                       |

Save History        Create Incident

                     |

                     |

              Admin Alert Email

```



---

# 📜 Employee History Module


Employees can view:


- Previous scans
- Uploaded files
- Risk levels
- Security decisions
- Scan timestamps



Example:


```
File:

salary_report.pdf


Risk:

HIGH


Action:

BLOCKED


Time:

2026-07-31

```



---

# 👤 Employee Profile Module


Employee profile displays:


- Employee ID
- Email
- Role
- Department Information



---

# 👑 Admin Dashboard Workflow


The administrator dashboard provides centralized security management.



## 1. Employee Monitoring


Admin can view:


- Registered employees
- Employee ID
- Email
- Department
- Role



Example:


```
Employee

Varun

Department:

CSE

Role:

USER

```



---

# 2. Security Statistics Dashboard


Admin dashboard displays:


- Total Employees
- Total Scans
- Blocked Attempts
- Security Alerts
- Total Incidents



Example:


```
Security Overview


Employees:

250


Total Scans:

1500


Blocked:

45


Alerts:

60


Incidents:

25

```



---

# 3. Risk Analytics


Admin can analyze:


- Safe activities
- Low-risk events
- Medium-risk events
- High-risk events
- Critical incidents



---

# 4. Incident Management System


When dangerous data leakage occurs:


```
High Risk Detection

        |

        |

Create Incident

        |

        |

Store Incident Details

        |

        |

Notify Administrator

```


Incident contains:


- Incident ID
- Employee ID
- File Name
- Risk Level
- Detected Data
- Timestamp
- Security Action



---

# 📧 Automated Admin Alert System


The system automatically sends email notifications during security violations.


Alert contains:


- Alert ID
- Generated Time
- Employee Details
- File Information
- Risk Level
- Detected Sensitive Data
- Security Action
- File Preview
- Security Recommendation



Example:


```
Dear Security Administrator,


A new DLP security alert has been generated.


Risk Level:

CRITICAL


Action:

BLOCKED


Please investigate immediately.

```



---

# 🧠 Machine Learning Module


The project contains an ML-based classification module.


ML Workflow:


```
Dataset Collection

        |

        |

Text Processing

        |

        |

Feature Extraction

        |

        |

Model Training

        |

        |

Risk Prediction

```



ML Components:


```
backend/app/ml/


├── ml_classifier.py

├── train_model.py

├── predict.py

├── model.pkl

└── vectorizer.pkl

```



---

# 🏛 System Architecture


```
                 USER

                  |

                  |

          Streamlit Frontend

                  |

                  |

             FastAPI Backend

                  |

      --------------------------------

      |                              |

 Authentication              Security Scanner

      |                              |

 Employee Database          AI Risk Analysis

      |                              |

      --------------------------------

                  |

            PostgreSQL Database

                  |

            Admin Dashboard

                  |

            Email Alert System

```



# 🛠 Technology Stack


## Frontend

- Python
- Streamlit
- Pandas
- Custom CSS


## Backend

- FastAPI
- SQLAlchemy
- REST API


## Database

- PostgreSQL


## AI / ML

- Machine Learning Classification
- Text Analysis
- Risk Prediction


## Document Processing

- pdfplumber
- python-docx


## Security

- Role-Based Authentication
- Data Validation
- Incident Management
- Security Logging



# 📂 Project Structure


```
AI-DLP-System

│
├── backend
│
│   ├── .env
│   ├── requirements.txt
│   └── test_service.py
│
│   └── app
│       │
│       ├── main.py
│       ├── database.py
│       ├── security.py
│       │
│       ├── ml
│       │   ├── ml_classifier.py
│       │   ├── train_model.py
│       │   ├── predict.py
│       │   ├── model.pkl
│       │   └── vectorizer.pkl
│       │
│       ├── models
│       │   ├── employee.py
│       │   ├── incident.py
│       │   └── dashboard.py
│       │
│       ├── routes
│       │   ├── auth.py
│       │   ├── scanner.py
│       │   ├── dashboard.py
│       │   ├── incident.py
│       │   └── admin_alert.py
│       │
│       ├── schemas
│       │   ├── employee.py
│       │   ├── incident.py
│       │   └── admin_alert.py
│       │
│       └── services
│           ├── employee_service.py
│           ├── scanner_service.py
│           ├── incident_service.py
│           ├── ml_service.py
│           ├── validate.py
│           └── admin_alert.py
│
│
├── dataset
│   ├── confidential_dataset.csv
│   ├── create_dataset.py
│   │
│   └── ml
│       ├── train_model.py
│       ├── predict.py
│       ├── model.pkl
│       └── vectorizer.pkl
│
│
└── frontend
    │
    ├── main.py
    ├── file_handler.py
    ├── validate.py
    ├── sidebar.py
    ├── email_sender.py
    ├── email_senders.py
    │
    ├── .streamlit
    │   └── config.toml
    │
    └── pages
        ├── login.py
        ├── sign.py
        ├── employee_dashboard.py
        ├── admin_dashboard.py
        ├── history.py
        ├── profile.py
        └── module1.py

```



# ▶️ Installation and Execution


## Backend Setup


```
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload

```


Backend:


```
http://127.0.0.1:8000

```


---

## Frontend Setup


```
cd frontend

streamlit run main.py

```



# 🌍 Real World Applications


## Banking Industry

Protection of:

- Customer information
- Financial records
- Account data


## Healthcare

Protection of:

- Patient records
- Medical documents


## IT Organizations

Protection of:

- Source code
- Internal files
- Business information


## Government Organizations

Protection of:

- Confidential records
- Citizen information



# ✅ Benefits


- Automated data protection
- Faster security analysis
- Reduced data leakage risk
- AI-based security decisions
- Complete audit tracking
- Enterprise security monitoring



# 🔮 Future Scope


Possible improvements:


- Real-time email monitoring
- Cloud deployment
- Advanced LLM security analysis
- User behaviour analytics
- SIEM integration
- Threat intelligence integration
- Enterprise security integration



# 📌 Project Information


## Project Name

AI-Powered Enterprise Data Leakage Prevention System


## Domain

Cybersecurity + Artificial Intelligence + Machine Learning


## Project Type

Full Stack Security Application


## Developed By


**Guntreddi Varun Kumar**

B.Tech Computer Science Engineering


Focus Areas:

- Cybersecurity
- Artificial Intelligence
- Machine Learning
- Full Stack Development
- Data Protection
