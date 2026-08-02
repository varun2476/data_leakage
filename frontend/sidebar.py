import streamlit as st


def employee_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <style>

            section[data-testid="stSidebar"]{
                background:#0f172a;
            }

            section[data-testid="stSidebar"] *{
                color:white;
            }

            </style>
            """,
            unsafe_allow_html=True
        )


        st.title("👨‍💼 Employee")


        st.write(
            f"Employee ID : {st.session_state.get('employee_id','')}"
        )


        st.divider()


        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):
            st.switch_page(
                "pages/employee_dashboard.py"
            )


        if st.button(
            "📄 Scan Document",
            use_container_width=True
        ):
            st.switch_page(
                "pages/module1.py"
            )


        if st.button(
            "📜 My History",
            use_container_width=True
        ):
            st.switch_page(
                "pages/history.py"
            )


        if st.button(
            "👤 Profile",
            use_container_width=True
        ):
            st.switch_page(
                "pages/profile.py"
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