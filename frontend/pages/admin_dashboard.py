import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# ==========================
# LOGIN CHECK
# ==========================

if "employee_id" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/login.py"
    )

    st.stop()



# ==========================
# ROLE CHECK
# ==========================

if st.session_state.role.lower() != "admin":

    st.error(
        "Access Denied. Admin only."
    )

    st.switch_page(
        "pages/employee_dashboard.py"
    )

    st.stop()



# ==========================
# CSS
# ==========================

st.markdown(
"""
<style>

.stApp{
    background:#0b1120;
}


header{
    visibility:hidden;
}


.card{

background:#111827;

padding:25px;

border-radius:15px;

border:1px solid #334155;

color:white;

text-align:center;

}


.metric-card{

background:#1e293b;

padding:20px;

border-radius:15px;

border:1px solid #334155;

}

</style>

""",
unsafe_allow_html=True
)



# ==========================
# SIDEBAR
# ==========================

with st.sidebar:


    st.title("🛡️ Admin Panel")


    st.write(
        f"""
Admin ID:

{st.session_state.employee_id}

Role:

{st.session_state.role}
"""
    )


    st.divider()


    if st.button(
        "🏠 Dashboard",
        use_container_width=True
    ):
        st.rerun()



    if st.button(
        "👥 Employee Management",
        use_container_width=True
    ):
        st.info(
            "Employee Management Coming Soon"
        )



    if st.button(
        "🚨 Incident Management",
        use_container_width=True
    ):
        st.info(
            "Incident Management Coming Soon"
        )



    if st.button(
        "📊 Risk Analytics",
        use_container_width=True
    ):
        st.info(
            "Risk Analytics Coming Soon"
        )



    if st.button(
        "🔔 Alert History",
        use_container_width=True
    ):
        st.info(
            "Alert History Coming Soon"
        )



    if st.button(
        "📄 Reports",
        use_container_width=True
    ):
        st.info(
            "Reports Coming Soon"
        )



    if st.button(
        "📜 System Logs",
        use_container_width=True
    ):
        st.info(
            "System Logs Coming Soon"
        )



    if st.button(
        "⚙ Settings",
        use_container_width=True
    ):
        st.info(
            "Settings Coming Soon"
        )



    st.divider()


    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.clear()

        st.switch_page(
            "pages/login.py"
        )




# ==========================
# HEADER
# ==========================


st.markdown(
"""
<div class="card">

<h1>
🛡️ Admin Dashboard
</h1>

<p>
AI Powered Data Leakage Prevention System
</p>

</div>

""",
unsafe_allow_html=True
)



st.write("")



# ==========================
# DASHBOARD METRICS
# ==========================


try:

    response = requests.get(
        "http://127.0.0.1:8000/dashboard/admin"
    )


    if response.status_code == 200:

        data=response.json()


    else:

        data={
            "employees":0,
            "active_users":0,
            "total_scans":0,
            "blocked":0,
            "alerts":0,
            "today_incidents":0
        }


except:

    data={
        "employees":0,
        "active_users":0,
        "total_scans":0,
        "blocked":0,
        "alerts":0,
        "today_incidents":0
    }




# ==========================
# CARDS
# ==========================


c1,c2,c3,c4,c5,c6 = st.columns(6)



with c1:

    st.metric(
        "👥 Total Employees",
        data["employees"]
    )


with c2:

    st.metric(
        "🟢 Active Users",
        data["active_users"]
    )


with c3:

    st.metric(
        "📄 Total Scans",
        data["total_scans"]
    )


with c4:

    st.metric(
        "🚫 Blocked Attempts",
        data["blocked"]
    )


with c5:

    st.metric(
        "🚨 Critical Alerts",
        data["alerts"]
    )


with c6:

    st.metric(
        "📅 Today's Incidents",
        data["today_incidents"]
    )



st.divider()



# ==========================
# RISK ANALYTICS
# ==========================


st.subheader(
    "📊 Risk Analytics"
)


# ==========================
# GET RISK ANALYTICS DATA
# ==========================

try:

    risk_response = requests.get(
        "http://127.0.0.1:8000/dashboard/admin/risk"
    )


    if risk_response.status_code == 200:

        risk_data = risk_response.json()

    else:

        risk_data = {
            "safe":0,
            "low":0,
            "medium":0,
            "high":0,
            "critical":0
        }


except Exception:

    risk_data = {
        "safe":0,
        "low":0,
        "medium":0,
        "high":0,
        "critical":0
    }
# ==========================
# RISK CARDS DISPLAY
# ==========================

risk_col1, risk_col2, risk_col3, risk_col4, risk_col5 = st.columns(5)


with risk_col1:

    st.metric(
        "🟢 Safe",
        risk_data["safe"]
    )


with risk_col2:

    st.metric(
        "🟢 Low",
        risk_data["low"]
    )


with risk_col3:

    st.metric(
        "🟡 Medium",
        risk_data["medium"]
    )


with risk_col4:

    st.metric(
        "🟠 High",
        risk_data["high"]
    )


with risk_col5:

    st.metric(
        "🔴 Critical",
        risk_data["critical"]
    )


st.divider()


# ==========================
# RECENT SYSTEM ACTIVITY
# ==========================

st.subheader(
    "📜 Recent System Activity"
)


st.info(
    "System logs will appear here"
)
# ==========================
# SYSTEM LOGS
# ==========================

st.subheader(
    "📜 Recent System Logs"
)


try:

    logs_response = requests.get(
        "http://127.0.0.1:8000/dashboard/admin/logs"
    )


    if logs_response.status_code == 200:

        logs = logs_response.json()


        if logs:

            logs_df = pd.DataFrame(logs)


            st.dataframe(
                logs_df,
                use_container_width=True
            )


        else:

            st.info(
                "No system logs available"
            )


    else:

        st.error(
            "Unable to load system logs"
        )


except Exception:

    st.error(
        "Backend server is not running"
    )