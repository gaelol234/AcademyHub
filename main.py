import streamlit as st


st.set_page_config(page_title="Academy Hub", page_icon=":material/school:", layout="wide", initial_sidebar_state="collapsed")

if not "user" in st.session_state:
    st.session_state["user"] = None
    
    st.switch_page("pages/login.py")
if st.session_state["user"] is None:
    st.switch_page("pages/login.py")


columns = st.columns([3,3,1,1,1,1,1])
with columns[0]:
    st.title("Academy Hub :material/school:")

if st.session_state["user"] is None:
    with columns[5]:
        if st.button("Login :material/login:", key = "login", use_container_width=True):
            st.switch_page("pages/login.py")

    with columns[6]:
        if st.button("Sign Up :material/assignment_ind:", key = "signup", use_container_width=True):
            st.switch_page("pages/sign_up.py")
else:
    with columns[6]:
        if st.button("Logout :material/logout:", key = "logout", use_container_width=True):
            st.session_state["user"] = None
            st.rerun()


st.write("---")

c = st.columns([6,1,1,1,1,1])

with c[1]:
    st.button("Robotics ", key="robotics", help="Robotics documentation", use_container_width=True)

with c[2]:
    st.button("  Data   ", key="data", help="Data documentation", use_container_width=True)

with c[3]:
    st.button("Embeddeds", key="embeddeds", help="Embeddeds documentation", use_container_width=True)

with c[4]:
    st.button("  Cyber  ", key="cybersecurity", help="CyberSecurity documentation", use_container_width=True)

with c[5]:
    st.button(" English ", key="english", help="English documentation", use_container_width=True)

c1 = st.columns([1,3,1])



with c1[1]:

    st.write("""
# Welcome to the UPY Academic Hub

The UPY Academic Hub is a centralized digital platform designed to support students at the Universidad Politécnica de Yucatán (UPY) in their academic journey. Our goal is to make it easier for students to access essential resources, such as majors, subjects per quarter, and open-access books, all in one place.

With this platform, you can:

- Find updated information about your courses and subjects.

- Access recommended open-access books for each subject.

- Save time by having all your academic resources centralized and easily searchable.

Whether you're studying robotics, data, or any other field, the UPY Academic Hub is here to help you succeed. Explore, learn, and make the most of your academic experience with us!
    """)