import streamlit as st


st.set_page_config(
    page_title="Employee Profile",
    page_icon="👤",
    layout="centered"
)


if "employee_id" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")
    st.stop()



st.title("👤 Employee Profile")


st.divider()


employee_id = st.session_state.get(
    "employee_id",
    "Not Available"
)


email = st.session_state.get(
    "email",
    "Not Available"
)


role = st.session_state.get(
    "role",
    "User"
)



st.markdown(
f"""
### Employee Information

**Employee ID**

{employee_id}


**Email**

{email}


**Role**

{role}

"""
)


st.divider()


if st.button("⬅ Back to Dashboard"):

    st.switch_page(
        "pages/employee_dashboard.py"
    )