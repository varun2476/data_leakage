import streamlit as st
import requests
import pandas as pd
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Employee Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

# -----------------------------
# Get Dashboard Data
# -----------------------------
if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()

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
with st.sidebar:

    st.title("👨‍💼 Employee")

    st.write(f"Employee ID: {st.session_state.employee_id}")

    st.divider()

    if st.button("🏠 Dashboard", use_container_width=True):
        st.rerun()

    if st.button("📄 Scan Document", use_container_width=True):
        st.switch_page("pages/module1.py")

    if st.button("📜 My History", use_container_width=True):
        st.switch_page("pages/history.py")

    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/profile.py")

    st.divider()

    
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

.card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
    text-align:center;
    color:white;
    box-shadow:0 10px 20px rgba(0,0,0,.3);
}

.title{
    font-size:40px;
    font-weight:bold;
    color:white;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<div class="card">
<h1 class="title">👨‍💼 Employee Dashboard</h1>
<p class="subtitle">
AI Powered Data Leakage Prevention System
</p>
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

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("📄 Total Scans", dashboard["total_scans"])

with col2:
    st.metric("✅ Safe Files", dashboard["safe_files"])


with col3:
    st.metric("🚫 Blocked Files", dashboard["blocked_files"])


with col4:
    st.metric("⚠ Risk Score", f'{dashboard["risk_score"]}%')

st.divider()

# ---------c--------------------
# Quick Actions
# -----------------------------

st.subheader("Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("📄 Scan Document",use_container_width=True):
        st.switch_page("pages/module1.py")

with c2:
    if st.button("📜 My History",use_container_width=True):
        st.info("History page coming soon.")
        st.switch_page("pages/history.py")
with c3:
    if st.button("👤 Profile",use_container_width=True):
        st.info("Profile page coming soon.")
        st.switch_page("pages/profile.py")
with c4:
    if st.button("🚪 Logout",use_container_width=True):

        st.session_state.clear()

        st.switch_page("pages/login.py")

st.divider()

# -----------------------------
# Recent Activity
# -----------------------------
st.subheader("Recent Activity")


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
            use_container_width=True
        )

    else:
        st.info("No recent scanning activity")


else:
    st.error("Unable to load recent activity")

st.divider()

# -----------------------------
# Logout
# -----------------------------

