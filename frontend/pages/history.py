import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="Scan History",
    page_icon="📜",
    layout="wide"
)


# Check login

if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()


employee_id = st.session_state.employee_id


# Title

st.title("📜 Scan History")

st.write(
    f"Employee ID : {employee_id}"
)


st.divider()


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
                use_container_width=True
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

if st.button("⬅ Back to Dashboard"):

    st.switch_page(
        "pages/employee_dashboard.py"
    )