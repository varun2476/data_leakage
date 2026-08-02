import streamlit as st
import requests
import pandas as pd
from sidebar import employee_sidebar
# -----------------------------
# Page Configuration
# -----------------------------



st.set_page_config(
    page_title="Scan History",
    layout="wide"
)



# -----------------------------
# Get Dashboard Data
# -----------------------------
if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()
employee_sidebar()
employee_id = st.session_state["employee_id"]

try:
    response = requests.get(
        f"http://127.0.0.1:8000/dashboard/employee/{employee_id}"
    )

    if response.status_code == 200:
        dashboard = response.json()
    else:
        dashboard = {
            "total_scans": 0,
            "safe_files": 0,
            "blocked_files": 0,
            "risk_score": 0
        }

except Exception:
    dashboard = {
        "total_scans": 0,
        "safe_files": 0,
        "blocked_files": 0,
        "risk_score": 0
    }


    
# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background:#0b1120;
}

header{
    visibility:hidden;
}

[data-testid="stToolbar"]{
    display:none;
}

/* Header */

.dashboard-header{
    background:linear-gradient(135deg,#1e293b,#111827);
    border:1px solid #334155;
    border-radius:18px;
    padding:35px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
}

.dashboard-header h1{
    color:white;
    font-size:48px;
    font-weight:700;
    margin-bottom:8px;
}

.dashboard-header p{
    color:#cbd5e1;
    font-size:20px;
}

/* Metric Cards */

.metric-card:hover{
    transform:translateY(-6px);
    border:1px solid #3b82f6;
}
.metric-card{
    background:#1e293b;
    border-radius:18px;
    padding:20px 16px;
    text-align:center;
    border:1px solid #334155;
    box-shadow:0 8px 20px rgba(0,0,0,.35);
    transition:.3s;
    margin-bottom:15px;
}

.metric-icon{
    font-size:30px;      /* Reduced from 50px */
    margin-bottom:8px;
}

.metric-title{
    color:#cbd5e1;
    font-size:15px;      /* Reduced from 17px */
    font-weight:600;
}

.metric-value{
    color:white;
    font-size:30px;      /* Reduced from 38px */
    font-weight:bold;
    margin-top:6px;
}





.section-title{
    color:white;
    font-size:30px;
    font-weight:bold;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)
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

def metric_card_small(icon, title, value, color="#38bdf8"):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-title">{title}</div>
        <div style="
            color:{color};
            font-size:19px;
            font-weight:600;
            margin-top:6px;
            word-break:break-word;
            overflow-wrap:anywhere;
        ">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<div class="dashboard-header">
<h1>👨‍💼 Employee Dashboard</h1>
<p>AI Powered Data Leakage Prevention System</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Welcome
# -----------------------------
email = st.session_state.get("email", "Not Available")
role = st.session_state.get("role", "User")
st.success(
    f"""
Welcome!

Employee ID : {st.session_state.employee_id}

Email : {email}

Role : {st.session_state.role}
"""
)

st.write("")

# -----------------------------
# Dashboard Cards
# -----------------------------



col1,col2,col3,col4 = st.columns(4)
last_file = dashboard["last_file"]

if len(str(last_file)) > 20:
    last_file = str(last_file)[:20] + "..."

last_scan = dashboard["last_scan"]

if last_scan:
    last_scan = str(last_scan).replace("T", " ")[:16]
else:
    last_scan = "-"

with col1:
    metric_card("📄","Total Scans",dashboard["total_scans"],"#38bdf8")

with col2:
    metric_card("✅","Safe Files",dashboard["safe_files"],"#22c55e")

with col3:
    metric_card("🚫","Blocked Files",dashboard["blocked_files"],"#ef4444")

with col4:
    metric_card("⚠","Risk Score",f'{dashboard["risk_score"]}%',"#f59e0b")
col5,col6,col7,col8 = st.columns(4)

with col5:
    metric_card("🔥","High Risk",dashboard["high_risk"],"#dc2626")

with col6:
    metric_card("📅","Today's Scans",dashboard["today_scans"],"#8b5cf6")

with col7:
    metric_card_small("📂", "Last File", last_file, "#06b6d4")

with col8:
    metric_card_small("🕒", "Last Scan", last_scan, "#10b981")

st.divider()

# ---------c--------------------
# Quick Actions
# -----------------------------

st.markdown(
    '<div class="section-title">⚡ Quick Actions</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("📄 Scan Document",width="stretch"):
        st.switch_page("pages/module1.py")

with c2:
    if st.button("📜 My History",width="stretch"):
        
        st.switch_page("pages/history.py")
with c3:
    if st.button("👤 Profile",width="stretch"):
        
        st.switch_page("pages/profile.py")
with c4:
    if st.button("🚪 Logout",width="stretch"):

        st.session_state.clear()

        st.switch_page("pages/login.py")

st.divider()

# -----------------------------
# Recent Activity
# -----------------------------
st.markdown(
    '<div class="section-title">📜 Recent Activity</div>',
    unsafe_allow_html=True
)


employee_id = st.session_state.employee_id


response = requests.get(
    f"http://127.0.0.1:8000/dashboard/employee/{employee_id}/recent"
)


if response.status_code == 200:

    data = response.json()

    if data:
        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch"
        )

    else:
        st.info("No recent scanning activity")


else:
    st.error("Unable to load recent activity")

st.divider()

# -----------------------------
# Logout
# -----------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("⬅ Back to login", width="stretch", key="back_dashboard"):
        st.switch_page("pages/login.py")

st.markdown("---")

st.caption(
    "Secure Data Scanner • AI Powered DLP • Version 1.0"
)

