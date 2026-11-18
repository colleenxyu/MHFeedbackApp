import pandas as pd
import streamlit as st
from supabase_client import supabase


st.set_page_config(
    page_title="Mey Han Onsite Feedback Program",
    page_icon="🍽",
    layout="wide"
)

USERNAME = st.secrets["program_username"]
PASSWORD = st.secrets["program_password"]

# Session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False



def login_screen():

    # Hide sidebar while on login page
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display:none;
    }

    [data-testid="stSidebarNav"] {
        display:none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Mey Han Feedback Program 🍽")
    st.subheader("User Login")

    username = st.text_input("Username", type="default")
    password = st.text_input("Password", type="password")

    if st.button("Enter Program"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.authenticated = True

            # Redirect to landing page
            st.switch_page("pages/01_NewFBReport.py")

        else:
            st.error("Incorrect login information")


if st.session_state.authenticated:

    # If already logged in, skip login page
    st.switch_page("pages/01_NewFBReport.py")

else:
    login_screen()