import streamlit as st
import time
from supabase import create_client, Client
import re

url: str = st.secrets.supabase.url
key: str = st.secrets.supabase.key
supabase: Client = create_client(url, key)



st.set_page_config(page_title="Sign up", page_icon=":material/assignment_ind:", layout="wide", initial_sidebar_state="collapsed")


st.title("Sign up :material/assignment_ind:")


if st.button("Login :material/login:", key = "login",):
    st.switch_page("pages/login.py")
st.write("---")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    if not re.search(r"@upy\.edu\.mx$", email):
        st.error("Email must end with @upy.edu.mx")
    else:
        response = supabase.auth.sign_up({"email": email, "password": password})
        st.info("Check your email for confirmation")
        time.sleep(2)
        st.switch_page("pages/login.py")
