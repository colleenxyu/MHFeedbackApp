import pandas as pd
import plotly.express as px
import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Feedback Report Search", page_icon="🍽", layout="wide")




# Security check
if not st.session_state.get("authenticated", False):
    st.switch_page("Main_Page.py")


def logout():

    st.session_state.authenticated = False
    st.switch_page("Main_Page.py")


# Sidebar
st.sidebar.image("MH_Logo1.png")
st.sidebar.title("Program Menu")

st.sidebar.page_link(
    "pages/01_NewFBReport.py",
    label="Enter New Report"
)

st.sidebar.page_link(
    "pages/02_FBReportSearch.py",
    label="Feedback Report Search"
)

st.sidebar.page_link(
    "pages/03_ReportDL.py",
    label="Feedback Report Download"
)

st.sidebar.page_link(
    "pages/04_GuidelinesPage.py",
    label="Guidelines Page"
)








if st.sidebar.button("Logout", type="tertiary"):
    logout()

#Program Proper
st.title("Mey Han Feedback Program")
st.header("Report Search")

@st.cache_resource
def init_supabase():
    url = st.secrets["supabase_URL"]
    key = st.secrets["supabase_Key"]
    return create_client (url, key)

supabase: Client = init_supabase()




st.write("This page is under construction.")
