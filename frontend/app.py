import streamlit as st
st.switch_page("pages/login.py")

def login_page():

    st.markdown(
        """
        <div class="login-container">

            <div class="logo">
                🔐
            </div>

            <h1>
                Secure Data Scanner
            </h1>

            <p>
                AI Powered Data Leakage Prevention System
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )


    password = st.text_input(
        "Password",
        placeholder="Enter your password",
        type="password"
    )


    col1, col2 = st.columns(2)


    with col1:
        remember = st.checkbox(
            "Remember me"
        )


    with col2:
        st.markdown(
            """
            <a class="forgot">
            Forgot Password?
            </a>
            """,
            unsafe_allow_html=True
        )



    if st.button("SIGN IN"):

        if email and password:

            st.success(
                "Login successful"
            )

        else:

            st.error(
                "Please enter email and password"
            )



    st.markdown(
        """
        <div class="signup">

        Don't have an account?
        <a>
        Create Account
        </a>

        </div>
        """,
        unsafe_allow_html=True
    )


login_page()