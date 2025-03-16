import streamlit as st
from supabase import create_client, Client
import re
import time


url: str = st.secrets.supabase.url
key: str = st.secrets.supabase.key
supabase: Client = create_client(url, key)



st.set_page_config(page_title="Login", page_icon=":material/login:", layout="wide", initial_sidebar_state="collapsed")



if st.session_state["user"] is not None:
    st.write("You are already logged in")
    time.sleep(2)
    st.switch_page("main.py")



st.title("Login :material/login:")


if st.button("Sign Up :material/assignment_ind:", key = "signup"):
    st.switch_page("pages/sign_up.py")
st.write("---")


email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if not re.search(r"@upy\.edu\.mx$", email):
        st.error("Email must end with @upy.edu.mx")
    else:

        cred = {"email": email, "password": password}
        try:
            response = supabase.auth.sign_in_with_password(cred).dict()
            with st.spinner("loading..."):
                time.sleep(2)
            if response["user"]:

                st.session_state["user"] = response["user"]
                st.success("Logged in")
                st.balloons()
                time.sleep(2)
                st.switch_page("main.py")
        except Exception as e:
            st.error(e)