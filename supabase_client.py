from supabase import create_client
import streamlit as st

supabase = create_client(
    st.secrets["supabase_URL"],
    st.secrets["supabase_Key"]
)

