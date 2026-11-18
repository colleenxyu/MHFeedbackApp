import pandas as pd
import plotly.express as px
import streamlit as st
from supabase_client import supabase
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
from io import BytesIO




st.set_page_config(page_title="Download Report", page_icon="🍽", layout="wide")


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







# Security check
if not st.session_state.get("authenticated", False):
    st.switch_page("Main_Page.py")


def logout():

    st.session_state.authenticated = False
    st.switch_page("Main_Page.py")



if st.sidebar.button("Logout", type="tertiary"):
    logout()

st.title("Mey Han Feedback Program")
st.header("Report Download")

st.write("This page is under construction.")