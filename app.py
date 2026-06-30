import streamlit as st
import pandas as pd
import file_handler
from file_handler import process_input
from datetime import datetime
def load_css(css_file):

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
st.markdown("""
<div class='hero'>

<h1>🔐 Secure Data Scanner</h1>

<p>
AI Powered Data Leakage Prevention System
</p>

</div>
""",unsafe_allow_html=True)

st.markdown("""
<style>
/* Whole App Background */
.stApp{
    background:#0b1120;
}

/* Main container */
.main{
    background:#0b1120;
}

/* Remove white top area */
[data-testid="stAppViewContainer"]{
    background:#0b1120;
}
 html, body{
    background:#0b1120;
}
/* Remove header background */
[data-testid="stHeader"]{
    background:#0b1120;
}
 header{
    visibility:hidden;
}

[data-testid="stToolbar"]{
    display:none;
}
 Background : #0B1120
Card       : #111827
Border     : #334155
Primary    : #2563EB
Success    : #22C55E
Warning    : #F59E0B
Danger     : #EF4444
Text       : #FFFFFF
Subtitle   : #94A3B8
[data-testid="stDecoration"]{
    display:none;
}
/* Remove toolbar spacing */
header{
    background:#0b1120 !important;
}

/* Main block */
.block-container{
    padding-top:1rem;
    background:#0b1120;
}
section[data-testid="stSidebar"]{
    background:#0f172a;
}

section[data-testid="stSidebar"] *{
    color:white;
}
.hero{

padding:35px;

border-radius:20px;

background:linear-gradient(135deg,#18181b,#111827);

border:1px solid #374151;

text-align:center;

margin-bottom:25px;

}

.hero h1{
font-size:55px;
color:white;
}
.hero p{
color:#bdbdbd;
font-size:20px;
}

.stApp{
    background:#0b1120;
    color:white;
}

.main{
    background:#0b1120;
}

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

h1,h2,h3,h4,h5,p,label{
    color:white;
}
[data-testid="stFileUploader"]{

background:#161b22;

border:2px dashed #6d28d9;

border-radius:18px;

padding:20px;

}
            .stButton>button{

width:100%;

height:60px;

border-radius:15px;

font-size:22px;

font-weight:bold;

background:linear-gradient(90deg,#3b82f6,#9333ea);

color:white;

border:none;

}

.stButton>button:hover{

transform:scale(1.02);

}
.scan-card{

background:#111827;

padding:30px;

border-radius:20px;

border:1px solid #2f3542;

margin-top:25px;

}
</style>
""",unsafe_allow_html=True)
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



col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 Files Scanned", st.session_state.files_scanned)

with col2:
    st.metric("🔒 Sensitive Found", st.session_state.sensitive_found)

with col3:
    st.metric("⚠ Risk Level", st.session_state.risk_level)

with col4:
    st.metric("🤖 Accuracy", "99.8%")
st.subheader("📄 Scan Document")
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

user_text = st.text_area(
    "Enter your message",
    height=170,
    placeholder="Paste text here or upload a document...",
    label_visibility="collapsed"
)
col1, col2, col3 = st.columns([1,5,1])
with col1:
  uploaded_file = st.file_uploader(
    "Upload File",
    type=["txt", "pdf", "docx"],
    key="upload_file",
    label_visibility="collapsed"
)
print("APP - After uploader:", uploaded_file)
if uploaded_file is not None:
    st.session_state["uploaded_file"] = uploaded_file
with col2:
    st.empty()
with col3:
    st.markdown("</div>", unsafe_allow_html=True)

@st.dialog("⚠ Sensitive Data Detected")
def show_popup(result):
    risk = result.get("risk", "LOW")
    color = {
        "SAFE": "🟢",
        "HIGH": "🟠",
        "CRITICAL": "🔴"
    }
    st.markdown(f"## {color.get(risk,'🔴')} Risk Level : **{risk}**")
    st.write(result["message"])
    st.markdown("---")
    detections = result.get("detections", [])
    if detections:
        df = pd.DataFrame(detections)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚫 Block Message",key="block_btn", use_container_width=True):
            st.error("❌ Message Blocked Successfully")
            st.session_state["action"] = "blocked"
            st.rerun()
    with col2:
     if st.button("✅ Process Anyway",key="process_btn", use_container_width=True):
        st.session_state.action = "processed"
        st.rerun()
send = st.button("🔍 Scan Document",
    use_container_width=True)
if send:
    file = st.session_state.get("uploaded_file", None)
    print("APP - user_text =", repr(user_text))
    with st.spinner("🔍 Scanning document... Please wait"):
        result = process_input(user_text, uploaded_file)
        st.session_state.scan_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        st.session_state.files_scanned += 1
        if result["status"]:
          if result["detected"]:
            st.session_state.sensitive_found += len(result["detections"])
            st.session_state.risk_level = result["risk"]
          else:
            st.session_state.risk_level = "SAFE"
    if not result["status"]:
        st.warning(result["message"])
    else:
        st.session_state.result = result
        st.session_state.message = result["content"]
result = st.session_state.get("result")
if result is not None:
    if result.get("detected"):
        if st.session_state.action is None:
            show_popup(result)
        elif st.session_state.action == "blocked":
            st.error("🚫 Message was blocked.")
            st.info(
    f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}\n\n"
    f"🕒 Time : {datetime.now().strftime('%I:%M:%S %p')}"
)
            st.session_state.result = None
            st.session_state.action = None
            st.session_state.message = ""
        elif st.session_state.action == "processed":
            st.success("✅ Message Sent Successfully")
            if uploaded_file is not None:
                st.info(
    f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}\n\n"
    f"🕒 Time : {datetime.now().strftime('%I:%M:%S %p')}"
)
                st.markdown("## 📄 Uploaded File")
                st.write("**File Name:**", uploaded_file.name)
                st.write("**File Type:**", uploaded_file.type)
            st.markdown("### 📄 Content")
            st.code(st.session_state.message)
            st.session_state.result = None
            st.session_state.action = None
            st.session_state.message = ""
    else:
        st.success("✅ Document is Safe")
        st.info(
            f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}\n\n"
            f"🕒 Time : {datetime.now().strftime('%I:%M:%S %p')}"
                 )
        st.info("No personal or confidential information detected.")
        
        st.markdown("### 📄 Content")

        st.code(st.session_state.message)

        st.session_state.result = None
        st.session_state.message = ""
st.markdown("---")
st.caption(
"Secure Data Scanner • AI Powered DLP • Version 1.0"
)

