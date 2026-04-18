import streamlit as st

st.set_page_config(page_title="Weather Dashboard", layout="wide")

# 🔐 Simple Login System
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.title("🔐 Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

# 🌗 Theme Toggle
theme = st.sidebar.radio("Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)

st.title("🌦️ Weather Intelligence Dashboard")
st.sidebar.success("Navigate using sidebar")