import streamlit as st


if "employee_id" not in st.session_state:
    st.switch_page("pages/login.py")
else:
    st.switch_page("pages/employee_dashboard.py")

st.set_page_config(
    page_title="Secure Data Scanner",
    page_icon="🔐",
    layout="wide"
)


# Redirect first time user to login

if "employee_id" not in st.session_state:

    st.switch_page(
        "pages/login.py"
    )


else:

    role = st.session_state.role.lower()


    if role == "admin":

        st.switch_page(
            "pages/admin_dashboard.py"
        )


    else:

        st.switch_page(
            "pages/employee_dashboard.py"
        )