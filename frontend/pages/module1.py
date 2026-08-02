import streamlit as st
import pandas as pd
import file_handler
from file_handler import process_input
from datetime import datetime
from email_senders import send_email
import email_senders
from email_validator import validate_email, EmailNotValidError
import sys
import os
import requests
from sidebar import employee_sidebar


st.set_page_config(
    page_title="Scan History",
    layout="wide"
)


employee_sidebar()

def scan_document_api(uploaded_file):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/scanner/analyze",
            files={
                "file":(
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
        )


        if response.status_code == 200:

            return response.json()


        else:

            st.error("Scanner API Failed")
            st.code(response.text)

            return {
                "status":False,
                "message":"API Error"
            }


    except Exception as e:

        st.error("Backend Connection Failed")
        st.code(str(e))

        return {
            "status":False,
            "message":"Connection Error"
        }

        

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()

st.markdown("""
<div class="dashboard-header">
    <h1>🔐 Secure Data Scanner</h1>
    <p>AI Powered Enterprise Data Leakage Prevention System</p>
</div>
""", unsafe_allow_html=True)
st.markdown(
"""
<style>

/* =========================
   GLOBAL APPLICATION
========================= */

.stApp {
    background:#0b1120;
}


/* Remove Streamlit top header */

header {
    visibility:hidden;
    height:0px;
}


[data-testid="stToolbar"] {
    display:none;
}


/* Main container */

[data-testid="stAppViewContainer"] {
    background:#0b1120;
}


[data-testid="stMainBlockContainer"] {
    background:#0b1120;
}


/* Content spacing */

.block-container {

    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;

}



/* =========================
   SIDEBAR
========================= */


section[data-testid="stSidebar"] {

    background:#0f172a !important;
    border-right:1px solid #1e293b;

}


section[data-testid="stSidebar"] > div {

    background:#0f172a !important;

}


/* Sidebar text */

section[data-testid="stSidebar"] * {

    color:white !important;

}



/* =========================
   DASHBOARD HEADER
========================= */


.dashboard-header {

    background:linear-gradient(135deg,#1e293b,#111827);

    border:1px solid #334155;

    border-radius:18px;

    padding:35px;

    text-align:center;

    margin-bottom:25px;

    box-shadow:0 8px 25px rgba(0,0,0,.35);

}


.dashboard-header h1 {

    color:white;

    font-size:46px;

}


.dashboard-header p {

    color:#cbd5e1;

    font-size:18px;

}



/* =========================
   CARDS
========================= */


.scan-card {

    background:#111827;

    border:1px solid #334155;

    border-radius:18px;

    padding:25px;

    margin-top:20px;

    box-shadow:0 8px 20px rgba(0,0,0,.35);

}



.metric-card {

    background:#1e293b;

    border-radius:18px;

    padding:18px;

    text-align:center;

    border:1px solid #334155;

    box-shadow:0 8px 20px rgba(0,0,0,.35);

}



.metric-icon {

    font-size:30px;

}



.metric-title {

    color:#cbd5e1;

    font-size:15px;

    font-weight:600;

}



.metric-value {

    color:white;

    font-size:28px;

    font-weight:bold;

}



/* =========================
   FILE UPLOADER
========================= */


[data-testid="stFileUploader"] {

    background:#161b22;

    border:2px dashed #3b82f6;

    border-radius:15px;

    padding:20px;

}



/* =========================
   BUTTON STYLE
========================= */


.stButton > button {

    width:100%;

    height:50px;

    border-radius:12px;

    background:linear-gradient(90deg,#2563eb,#7c3aed);

    color:white;

    border:none;

    font-size:18px;

    font-weight:600;

}



.stButton > button:hover {

    transform:scale(1.02);

    border:1px solid #60a5fa;

}



/* =========================
   REMOVE STREAMLIT WHITE GAP
========================= */


/* Left sidebar + main divider */

[data-testid="stSidebar"] {

    min-width:260px;

}


/* Main area beside sidebar */

.main {

    background:#0b1120;

}



/* Fix blank right/side background */

[data-testid="stAppViewContainer"] > section {

    background:#0b1120;

}


</style>
""",
unsafe_allow_html=True
)

if "action" not in st.session_state:
    st.session_state.action = None

if "result" not in st.session_state:
    st.session_state.result = None

if "message" not in st.session_state:
    st.session_state.message = ""
if "scan_time" not in st.session_state:
    st.session_state.scan_time = ""


if "files_scanned" not in st.session_state:
    st.session_state.files_scanned = 0

if "sensitive_found" not in st.session_state:
    st.session_state.sensitive_found = 0

if "risk_level" not in st.session_state:
    st.session_state.risk_level = "--"

def metric_card(icon, title, value, color="#38bdf8"):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color:{color};">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)
col1,col2,col3,col4 = st.columns(4)

with col1:
    metric_card("📄","Files Scanned",st.session_state.files_scanned,"#38bdf8")

with col2:
    metric_card("🔒","Sensitive Found",st.session_state.sensitive_found,"#22c55e")

with col3:
    metric_card("⚠","Risk Level",st.session_state.risk_level,"#f59e0b")

with col4:
    metric_card("🤖","Accuracy","99.8%","#8b5cf6")
if st.session_state.scan_time:
    st.markdown(
        f"<span style='color:white;'><b>🕒 Last Scan:</b> {st.session_state.scan_time}</span>",
        unsafe_allow_html=True
    )




st.markdown(
    "<p style='color:white; font-weight:bold;'>📧 Receiver Email</p>",
    unsafe_allow_html=True
)

recipient_email = st.text_input(
    label="Receiver Email",
    label_visibility="collapsed",
    placeholder="example@gmail.com",
)

st.markdown(
    "<h2 style='color:white;'>📄 Place  Document Here </h2>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "📂 Upload Document",
    type=["txt", "pdf", "docx"],
    key="upload_file"
)

if uploaded_file is not None:

    st.session_state["uploaded_file"] = uploaded_file

    scan_result = process_input(uploaded_file=uploaded_file)

    if scan_result["status"]:
        st.session_state["original_content"] = scan_result["content"]
@st.dialog("⚠ Sensitive Data Detected")
def show_popup(result):
    risk = result.get("risk", "LOW")
    color = {
        "SAFE": "🟢",
        "HIGH": "🟠",
        "CRITICAL": "🔴"
    }
    st.markdown(f"## {color.get(risk,'🔴')} Risk Level : **{risk}**")
    st.write(
    result.get(
        "message",
        "Sensitive information detected"
    )
)
    st.markdown("---")
    detections = result.get("detections", [])
    if detections:
        df = pd.DataFrame(detections)
        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚫 Block Message",key="block_btn", width="stretch"):
            try:
                response = requests.post(
                        "http://127.0.0.1:8000/incident/create",
                         json={

                "employee_id": st.session_state.employee_id,

                "file_name": uploaded_file.name,

                "receiver_email": recipient_email,

                "risk_level": result.get("risk"),

                "status": "BLOCKED",

                "action": "BLOCKED",

                "detected_data": str(
                    result.get("detections",[])
                ),

                "llm_prediction": result.get(
    "llm_prediction",
    "Sensitive"
),

               "confidence": str(
    result.get(
        "confidence",
        "95%"
    )
),

"confidentiality": result.get(
    "confidentiality",
    "Confidential"
)

            }
        )
                if response.status_code == 200:

                      st.success("Blocked file saved successfully")
                else:

                      st.error( "Database save failed")      
            except Exception as e:
                    st.error("Backend connection error")
                    st.write(e)
            st.session_state["action"] = "blocked"   
            st.rerun()
    with col2:
     if st.button("✅ Process Anyway",key="process_btn", width="stretch"):
        st.session_state.action = "processed"
        st.rerun()
send = st.button("🔍 Scan Document",width="stretch")
st.markdown("</div>", unsafe_allow_html=True)
if send:

    if uploaded_file is None:

        st.error("❌ Please upload a document")

    else:

        with st.spinner("🔍 Scanning document... Please wait"):


            result = scan_document_api(uploaded_file)


            if result.get("status"):


                scan_data = result["result"]

                


                st.session_state.scan_time = datetime.now().strftime(
                    "%d-%m-%Y %I:%M:%S %p"
                )


                st.session_state.files_scanned += 1



                if scan_data.get("detected"):


                    st.session_state.sensitive_found += len(
                        scan_data.get("detections", [])
                    )


                    st.session_state.risk_level = scan_data.get(
                        "risk",
                        "UNKNOWN"
                    )


                else:

                    st.session_state.risk_level = "SAFE"



                st.session_state.result = scan_data

                st.session_state.message = uploaded_file.name



            else:

                st.error(result.get("message"))
scan_result = st.session_state.get("result")
if scan_result is not None:
    if scan_result.get("detected"):
        if st.session_state.action is None:
            show_popup(scan_result)
        elif st.session_state.action == "blocked":
              st.error("🚫 Message was blocked.")
              st.info(
                 f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}\n\n"
                 f"🕒 Time : {datetime.now().strftime('%I:%M:%S %p')}"
              )
              st.markdown(
                          "<h3 style='color:white;'>📄 File Details</h3>",
                          unsafe_allow_html=True
                      )
                      
              st.markdown(
                          f"<span style='color:white;'><b>File Name:</b> {uploaded_file.name}</span>",
                          unsafe_allow_html=True
                      )
                      
              st.markdown(
                          f"<span style='color:white;'><b>File Type:</b> {uploaded_file.type}</span>",
                          unsafe_allow_html=True
                      )
              st.session_state.result = None
              st.session_state.action = None
              st.session_state.message = ""
              st.stop()
        elif st.session_state.action == "processed":

            # Get email body
            email_body = (
    "File Scanned: "
    + uploaded_file.name
    + "\n\nDetected Data:\n"
    + str(scan_result.get("detections"))
)


            # Validate receiver email
            if recipient_email.strip() == "":
                st.error("❌ Please enter receiver email.")
                st.stop()


            try:
                validate_email(recipient_email.strip())

            except EmailNotValidError:
                st.error("❌ Invalid Email Address")
                st.stop()


            # Send incident to FastAPI backend
            try:
                response = requests.post(
    "http://127.0.0.1:8000/admin/alert",
    json={
        "employee_id": st.session_state["employee_id"],
        "file_name": uploaded_file.name,
        "risk_level": scan_result.get("risk"),
        "detected_data": str(scan_result.get("detections", [])),
        "sender_email": st.session_state["email"],
        "receiver_email": recipient_email,
        "file_content": st.session_state["original_content"],
    }
)
                  
                incident_response = requests.post("http://127.0.0.1:8000/incident/create",
                    json={

    "employee_id": st.session_state.employee_id,

    "file_name": uploaded_file.name,

    "receiver_email": recipient_email,

    "risk_level":scan_result.get("risk"),

    "status":"BYPASSED",

    "action":"PROCESSED",

    "detected_data":str(
            scan_result.get("detections",[])
        ),

    "llm_prediction": scan_result.get(
            "llm_prediction",
            "Sensitive"
        ),

    
    "confidence": str(
    scan_result.get(
        "confidence",
        "N/A"
    )
),

    "confidentiality": scan_result.get(
    "confidentiality",
    "Unknown"
)

}

)
                print(scan_result)
                if incident_response.status_code != 200:

                    st.success("Incident save failed") 

                             

                if response.status_code == 200:

                    data = response.json()

                    st.success(
            "✅ Message Delivered Successfully"
        )

                   

                    st.info(
            f"Alert Time: {data['alert_time']}"
        )

                else:

                    st.error(
            "❌ Admin notification failed"
        )

                    st.code(response.text)


            except Exception as e:

                    st.error(
        "❌ Backend connection failed"
    )

                    


            # Display uploaded file details
            if uploaded_file is not None:

                st.markdown(
    "<h3 style='color:white;'>📄 File Details</h3>",
    unsafe_allow_html=True
)

                st.markdown(
    f"<span style='color:white;'><b>File Name:</b> {uploaded_file.name}</span>",
    unsafe_allow_html=True
)

                st.markdown(
    f"<span style='color:white;'><b>File Type:</b> {uploaded_file.type}</span>",
    unsafe_allow_html=True
)

            

            # Clear session
            st.session_state.result = None

            st.session_state.action = None

            st.session_state.message = ""
        
    else:
        st.success("✅ Document is Safe")
        # Prepare email body
        email_body = st.session_state.get("message", "")

    # If no message is stored, use user text
        if email_body.strip() == "":
            email_body = uploaded_file.name

    # If a file was uploaded and extracted, use result content
        if st.session_state.result is not None:
                email_body = st.session_state.result.get(
                    "content",
                    email_body
    )
    # Send email
        if recipient_email.strip() == "":
            st.error("❌ Please enter receiver email.")
        else:
            try:
                validate_email(recipient_email.strip())
            except EmailNotValidError:
                st.error("❌ Invalid Email Address")
                st.stop()
            email_result = send_email(
            receiver=recipient_email.strip(),
            subject="Secure Data Scanner Report",
            body=email_body
        )

            if email_result is True:
                
                st.success("📧 Email Sent Successfully!")
                incident_response =requests.post(
    "http://127.0.0.1:8000/incident/create",
    json={

    "employee_id": st.session_state.employee_id,

    "file_name": uploaded_file.name,

    "receiver_email": recipient_email,

    "risk_level": "LOW",

    "status": "safe",

    "action":"ALLOWED",

    "detected_data": str(scan_result.get("detections")),

    "llm_prediction": "Safe",

    "confidence":"safe",

    "confidentiality": "Public",

}
)
                
            else:
                st.error("❌ Email Sending Failed")
                st.error("e-mail is does not exist please enter valid emaild ID")
                st.code(email_result)
                st.stop()
        st.info(
            f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}\n\n"
            f"🕒 Time : {datetime.now().strftime('%I:%M:%S %p')}"
                 )
        
        st.markdown(
            "<h3 style='color:white;'>📄 File Details</h3>",
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"<span style='color:white;'><b>File Name:</b> {uploaded_file.name}</span>",
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"<span style='color:white;'><b>File Type:</b> {uploaded_file.type}</span>",
            unsafe_allow_html=True
        )
        st.info("No personal or confidential information detected.")
        

        st.session_state.result = None
        st.session_state.message = ""
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("⬅ Back to Dashboard", width="stretch", key="back_dashboard"):
        st.switch_page("pages/employee_dashboard.py")

st.markdown("---")

st.caption(
    "Secure Data Scanner • AI Powered DLP • Version 1.0"
)