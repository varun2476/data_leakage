import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛡️",
    layout="wide"
)
# ==========================
# PAGE STATE
# ==========================

if "admin_page" not in st.session_state:
    st.session_state.admin_page = "Dashboard"

st.sidebar.markdown(
"""
<style>

[data-testid="stSidebar"]{
    background:#111827;
}

[data-testid="stSidebar"] *{
    color:white;
}

</style>
""",
unsafe_allow_html=True
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

st.markdown("""
<style>

.stApp{
    background:#0b1120;
}

/* Hide Streamlit Header */
header{
    display:none;
}
/* Dashboard Header */
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
    margin-bottom:8px;
    font-weight:700;
}

.dashboard-header p{
    color:#cbd5e1;
    font-size:20px;
}

/* Metric Cards */

.metric-card{

    background:#1e293b;
    border-radius:18px;
    padding:28px 20px;
    text-align:center;
    border:1px solid #334155;
    transition:0.3s;
    box-shadow:0px 6px 15px rgba(0,0,0,.35);
    margin-bottom:20px;

}

.metric-card:hover{

    transform:translateY(-6px);
    border:1px solid #3b82f6;

}

.metric-icon{

    font-size:50px;
    margin-bottom:12px;

}

.metric-title{

    color:#cbd5e1;
    font-size:18px;
    font-weight:600;

}

.metric-value{

    color:white;
    font-size:42px;
    font-weight:bold;
    margin-top:12px;

}

/* Section Title */

.section-title{

    color:white;
    font-size:34px;
    font-weight:bold;
    margin-top:25px;
    margin-bottom:15px;

}
/* Extra Dashboard Cards */

.info-card{

    background:#1e293b;
    border-radius:18px;
    padding:25px;
    text-align:center;
    border:1px solid #334155;
    margin-bottom:20px;

}


.info-title{

    color:#cbd5e1;
    font-size:18px;

}


.info-value{

    color:white;
    font-size:35px;
    font-weight:bold;

}


.status-box{

    background:#1e293b;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
    color:white;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"]{
    background:#111827;
}


/* Sidebar normal text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:white;
}


/* Sidebar buttons */
section[data-testid="stSidebar"] button{

    background:#2563eb;
    color:white;

    border:none;
    border-radius:10px;

    height:45px;

    font-size:16px;
    font-weight:600;

}


/* Button hover */

section[data-testid="stSidebar"] button:hover{

    background:#1d4ed8;
    color:white;

}


/* Divider */

section[data-testid="stSidebar"] hr{

    border-color:#334155;

}

</style>
""",
unsafe_allow_html=True)
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


    menu = [
        "🏠 Dashboard",
        "📊 Risk Analytics",
        "📡 Real Time Security Overview",
        "🚨 Live Threat Monitor",
        "👨‍💻 Employee Activity",
        "🤖 AI Detection Insights",
        "📂 File Monitoring",
        "🔐 Policy Management",
        "📜 System Logs",
        "⚙ System Health"
    ]


    for item in menu:

        if st.button(
            item,
            use_container_width=True
        ):

            st.session_state.admin_page = item



    st.divider()


    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.clear()

        st.switch_page(
            "pages/login.py"
        )




st.markdown("""
<div class="dashboard-header">
<h1>🛡️ Admin Dashboard</h1>
<p>AI Powered Data Leakage Prevention System</p>
</div>
""", unsafe_allow_html=True)


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
def metric_card(icon,title,value,color="#60a5fa"):

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color:{color};">
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.admin_page == "🏠 Dashboard":

    st.markdown(
    """
    <div class="section-title">
    🏠 Dashboard Overview
    </div>
    """,
    unsafe_allow_html=True
    )
    c1,c2,c3,c4,c5,c6 = st.columns(6)

    with c1:
         metric_card("👥","Employees",data["employees"],"#38bdf8")

    with c2:
        metric_card("🟢","Active Users",data["active_users"],"#22c55e")

    with c3:
        metric_card("📄","Total Scans",data["total_scans"],"#facc15")

    with c4:
        metric_card("🚫","Blocked files",data["blocked"],"#fb923c")

    with c5:
        metric_card("🚨","Alerts files",data["alerts"],"#ef4444")

    with c6:
        metric_card("📅","Incidents",data["today_incidents"],"#a855f7")




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
if st.session_state.admin_page == "📊 Risk Analytics":
    st.markdown('<div class="section-title">📊 Risk Analytics</div>', unsafe_allow_html=True)

    r1,r2,r3,r4,r5=st.columns(5)

    with r1:
        metric_card("🟢","Safe",risk_data["safe"],"#22c55e")

    with r2:
        metric_card("🟢","Low",risk_data["low"],"#4ade80")

    with r3:
        metric_card("🟡","Medium",risk_data["medium"],"#eab308")

    with r4:
        metric_card("🟠","High",risk_data["high"],"#f97316")

    with r5:
        metric_card("🔴","Critical",risk_data["critical"],"#ef4444")



if st.session_state.admin_page == "📡 Real Time Security Overview":

        st.markdown(
        """
        <div class="section-title">
📡      Real Time Security Overview
        </div>
        """,
        unsafe_allow_html=True
        )
        e1,e2,e3,e4,e5,e6 = st.columns(6)


        with e1:
            metric_card("📧","Emails Scanned",245)

        with e2:
            metric_card("🛑","Leak Attempts",18)

        with e3:
            metric_card("🔐","Policy Violations",7)

        with e4:
            metric_card("🟢","Online Users",12)

        with e5:
            metric_card("🤖","AI Predictions",156)

        with e6:
            metric_card("⚠","False Positive",3)
        



if st.session_state.admin_page == "🚨 Live Threat Monitor":

    st.markdown(
    """
    <div class="section-title">
    🚨 Live Threat Monitor
    </div>
    """,
    unsafe_allow_html=True
    )
    threats = pd.DataFrame(
    [
    {
"Time":"10:30",
"Employee":"Varun",
"File":"salary.pdf",
"Risk":"HIGH",
"Action":"BLOCKED"
},

{
"Time":"10:35",
"Employee":"Dilip",
"File":"report.docx",
"Risk":"MEDIUM",
"Action":"ALLOWED"
}

]
)


    st.dataframe(
    threats,
    use_container_width=True,
    hide_index=True
)


if st.session_state.admin_page == "👨‍💻 Employee Activity":

    st.markdown(
    """
    <div class="section-title">
    👨‍💻 Employee Activity
    </div>
    """,
    unsafe_allow_html=True
    )
    employee_activity=pd.DataFrame(
    [
    {
"Employee":"Varun",
"Department":"IT",
"Status":"Online",
"Files":20,
"Risk":"30%"
},

{
"Employee":"Dilip",
"Department":"HR",
"Status":"Offline",
"Files":10,
"Risk":"70%"
}

]
)


    st.dataframe(
    employee_activity,
use_container_width=True,
hide_index=True
)


if st.session_state.admin_page == "🤖 AI Detection Insights":
    st.markdown(
    """
    <div class="section-title">
    🤖 AI Detection Insights
    </div>
    """,
    unsafe_allow_html=True
    )


    a1,a2,a3,a4=st.columns(4)


    with a1:
        metric_card(
        "🎯",
        "AI Accuracy",
        "92%"
    )


    with a2:
        metric_card(
        "🔍",
        "Sensitive Found",
        340
    )


    with a3:
        metric_card(
        "🧠",
        "AI Predictions",
        156
    )


    with a4:    
        metric_card(
        "⚠",
        "False Alerts",
        5
    )
# ==========================
# RISK CARDS DISPLAY
# =========================
# ==========================
# FILE MONITORING
# ==========================

if st.session_state.admin_page == "📂 File Monitoring":

    st.markdown(
    """
    <div class="section-title">
    📂 File Monitoring
    </div>
    """,
    unsafe_allow_html=True
    )


    files = pd.DataFrame(
    [
        {
            "File":"salary.pdf",
            "Employee":"Varun",
            "Type":"PDF",
            "Status":"Blocked",
            "Risk":"HIGH"
        },

        {
            "File":"report.docx",
            "Employee":"Dilip",
            "Type":"DOCX",
            "Status":"Allowed",
            "Risk":"MEDIUM"
        }
    ]
    )


    st.dataframe(
        files,
        use_container_width=True,
        hide_index=True
    )



# ==========================
# POLICY MANAGEMENT
# ==========================

if st.session_state.admin_page == "🔐 Policy Management":

    st.markdown(
    """
    <div class="section-title">
    🔐 Policy Management
    </div>
    """,
    unsafe_allow_html=True
    )


    policies = pd.DataFrame(
    [
        {
            "Policy":"Email Data Protection",
            "Status":"Active"
        },

        {
            "Policy":"Sensitive File Blocking",
            "Status":"Active"
        },

        {
            "Policy":"External Sharing Restriction",
            "Status":"Active"
        }
    ]
    )


    st.dataframe(
        policies,
        use_container_width=True,
        hide_index=True
    )



# ==========================
# SYSTEM LOGS
# ==========================

if st.session_state.admin_page == "📜 System Logs":

    st.markdown(
    """
    <div class="section-title">
    📜 System Logs
    </div>
    """,
    unsafe_allow_html=True
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
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info(
                    "No system logs available"
                )


        else:

            st.error(
                "Unable to load logs"
            )


    except:

        st.error(
            "Backend server not running"
        )



# ==========================
# SYSTEM HEALTH
# ==========================

if st.session_state.admin_page == "⚙ System Health":

    st.markdown(
    """
    <div class="section-title">
    ⚙ System Health
    </div>
    """,
    unsafe_allow_html=True
    )


    health = pd.DataFrame(
    [
        {
            "Service":"FastAPI",
            "Status":"🟢 Running"
        },

        {
            "Service":"Database",
            "Status":"🟢 Connected"
        },

        {
            "Service":"AI Model",
            "Status":"🟢 Loaded"
        },

        {
            "Service":"Email Service",
            "Status":"🟢 Active"
        }
    ]
    )


    st.dataframe(
        health,
        use_container_width=True,
        hide_index=True
    )


# ==========================
# SYSTEM LOGS
# ==========================




