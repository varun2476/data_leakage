import streamlit as st
import requests
import pandas as pd
from sidebar import employee_sidebar
st.set_page_config(
    page_title="Scan History",
    layout="wide"
)

employee_sidebar()

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
    padding:28px;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0 8px 20px rgba(0,0,0,.35);
}

.dashboard-header h1{
    color:white;
    font-size:40px;
    margin-bottom:8px;
}

.dashboard-header p{
    color:#cbd5e1;
    font-size:18px;
}

/* Info Card */

.info-card{
    background:#111827;
    border:1px solid #334155;
    border-radius:15px;
    padding:18px;
    color:white;
    margin-bottom:20px;
    font-size:18px;
}

/* Table */

[data-testid="stDataFrame"]{
    border:1px solid #334155;
    border-radius:15px;
}

/* Buttons */

.stButton>button{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 20px;
    font-size:16px;
    font-weight:600;
}

.stButton>button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)



# Check login

if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()


employee_id = st.session_state.employee_id


# Title

st.markdown("""
<div class="dashboard-header">
<h1>📜 Scan History</h1>
<p>View Your Previous Document Scans</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="info-card">
<b>Employee ID :</b> {employee_id}
</div>
""", unsafe_allow_html=True)


# Get history from backend

try:

    response = requests.get(
    f"http://127.0.0.1:8000/dashboard/employee/{employee_id}/history"
)
    if response.status_code == 200:

        history = response.json()
        if history:

            df = pd.DataFrame(history)


            st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    
)


        else:

            st.info(
                "No scan history found"
            )


    else:

        st.error(
            "Unable to fetch history"
        )


except Exception as e:

    st.error(
        "Backend server is not running"
    )



st.divider()


# Back button

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("⬅ Back to Dashboard", use_container_width=True):
        st.switch_page("pages/employee_dashboard.py")