import streamlit as st
import requests
import time
st.set_page_config(
    page_title="Secure Data Scanner Login",
    page_icon="🔐",
    layout="centered"
)


# ==========================
# CSS DESIGN
# ==========================

st.markdown(
"""
<style>

/* Whole Application */

.stApp{

    background:#0b1120;

}


/* Remove Streamlit Header */

header{

    visibility:hidden;

}


[data-testid="stToolbar"]{

    display:none;

}


/* Main Container */

.block-container{

    padding-top:2rem;

    max-width:500px;

}


/* Login Card */

.login-card{

    background:#111827;

    padding:40px;

    border-radius:25px;

    border:1px solid #334155;

    box-shadow:
    0 20px 40px rgba(0,0,0,0.5);

    text-align:center;

}


/* Logo */

.logo{

    font-size:70px;

}



/* Title */

.login-card h1{

    color:white;

    font-size:35px;

    margin-bottom:10px;

}



/* Subtitle */

.login-card p{

    color:#94a3b8;

    font-size:18px;

}



/* Input Labels */

label{

    color:white !important;

    font-weight:600;

}



/* Input Box */

.stTextInput input{

    background:#1e293b;

    color:white;

    border:1px solid #334155;

    border-radius:12px;

    height:45px;

}



/* Button */

.stButton button{


    width:100%;


    height:50px;


    border-radius:15px;


    background:
    linear-gradient(
    90deg,
    #2563eb,
    #9333ea
    );


    color:white;


    font-size:20px;


    font-weight:bold;


    border:none;


}



.stButton button:hover{

    transform:scale(1.03);

}


/* Forgot Password */

.forgot{

    color:#38bdf8;

    text-align:right;

    cursor:pointer;

}



/* Signup */

.signup{

    text-align:center;

    color:#94a3b8;

    margin-top:25px;

}



.signup span{

    color:#38bdf8;

    font-weight:bold;

}



</style>

""",
unsafe_allow_html=True
)



# ==========================
# LOGIN UI
# ==========================


st.markdown(
"""
<div class="login-card">

<div class="logo">
🔐
</div>


<h1>
Secure Data Scanner
</h1>


<p>
AI-Powered Enterprise Data Leakage Prevention System
</p>


</div>

""",
unsafe_allow_html=True
)


st.write("")


# ==========================
# INPUT FIELDS
# ==========================

email = st.text_input(
    "📧 Email Address",
    placeholder="Enter your email"
)


password = st.text_input(
    "🔑 Password",
    placeholder="Enter your password",
    type="password"
)

role = st.selectbox(
    "👔 Role",
    [ "user", "admin"]
)
col1,col2 = st.columns(2)


with col1:

    st.checkbox(
        "Remember me"
    )


with col2:

    st.markdown(
    """
    <div class="forgot">
    Forgot Password?
    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")


# ==========================
# LOGIN API CONNECTION
# ==========================

if st.button("SIGN IN"):


    if email and password and role :


        try:

            response = requests.post(

                "http://127.0.0.1:8000/auth/login",

                json={
                    "email": email,
                    "password": password,
                    "role":role.lower()
                }

            )


            if response.status_code == 200:


                data = response.json()
                

                # Store login details

                st.session_state.employee_id = data["user_id"]

                st.session_state.role = data["role"]
                st.session_state.email = data["email"]
                

                # Role based navigation

                user_role = data["role"].lower()
                st.write("Backend Role:", user_role)

                if user_role == "admin":

                    st.success("Admin Login Successful")

                    time.sleep(1)   

                    st.switch_page(
        "pages/admin_dashboard.py"
    )


                elif user_role == "user":

                    st.success("User Login Successful")

                    time.sleep(1)

                    st.switch_page("pages/employee_dashboard.py")


                else:

                         st.error("Unknown role")


            else:


                error = response.json()


                st.error(
                    error.get(
                        "detail",
                        "Invalid email or password"
                    )
                )



        except Exception as e:


            st.error(
                "Backend server is not running"
            )

            st.write(e)



    else:


        st.warning(
            "Please enter email and password"
        )

# ==========================
# SIGNUP LINK
# ==========================
st.markdown(
"""
<div class="signup">
Don't have an account?
</div>
""",
unsafe_allow_html=True
)

if st.button("📝 Create Account", use_container_width=True):
    st.switch_page("pages/sign.py")