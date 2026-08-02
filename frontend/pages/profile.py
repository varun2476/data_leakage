import streamlit as st
from sidebar import employee_sidebar
from sidebar import employee_sidebar
st.set_page_config(
    page_title="Employee Profile",
    layout="wide"
)



# -----------------------------
# Login Check
# -----------------------------
if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()
employee_sidebar()
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
    padding:30px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0 8px 20px rgba(0,0,0,.35);
}

.dashboard-header h1{
    color:white;
    font-size:42px;
    margin-bottom:8px;
}

.dashboard-header p{
    color:#cbd5e1;
    font-size:18px;
}

/* Profile Card */

.profile-card{
    background:#111827;
    border:1px solid #334155;
    border-radius:18px;
    padding:30px;
    color:white;
    box-shadow:0 8px 20px rgba(0,0,0,.35);
    margin-bottom:20px;
}

.profile-row{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:18px 0;
    border-bottom:1px solid #334155;
}

.profile-row:last-child{
    border-bottom:none;
}

.profile-label{
    color:#94a3b8;
    font-size:18px;
    font-weight:600;
}

.profile-value{
    color:white;
    font-size:20px;
    font-weight:bold;
}

/* Button */

.stButton>button{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    font-weight:600;
}

.stButton>button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# User Data
# -----------------------------

employee_id = st.session_state.get("employee_id", "Not Available")
email = st.session_state.get("email", "Not Available")
role = st.session_state.get("role", "User")
department = st.session_state.get("department", "Not Available")

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<div class="dashboard-header">
    <h1>👤 Employee Profile</h1>
    <p>Manage Your Account Information</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Profile Information
# -----------------------------

st.markdown(f"""
<div class="profile-card">

<div class="profile-row">
<span class="profile-label">🆔 Employee ID</span>
<span class="profile-value">{employee_id}</span>
</div>

<div class="profile-row">
<span class="profile-label">📧 Email</span>
<span class="profile-value">{email}</span>
</div>

<div class="profile-row">
<span class="profile-label">👤 Role</span>
<span class="profile-value">{role}</span>
</div>
<div class="profile-row">
<span class="profile-label">👤 department</span>
<span class="profile-value">{department}</span>
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Back Button
# -----------------------------

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("⬅ Back to Dashboard", use_container_width=True):
        st.switch_page("pages/employee_dashboard.py")