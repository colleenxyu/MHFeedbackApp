import io
import pandas as pd
import plotly.express as px
import streamlit as st
from docxtpl import DocxTemplate
from supabase_client import supabase

# Page Configuration
st.set_page_config(page_title="New Feedback Report", page_icon="🍽", layout="wide")

# Security check
if not st.session_state.get("authenticated", False):
    st.switch_page("Main_Page.py")


def logout():
    st.session_state.authenticated = False
    st.switch_page("Main_Page.py")


# Sidebar
st.sidebar.image("MH_Logo1.png")
st.sidebar.title("Program Menu")

st.sidebar.page_link("pages/01_NewFBReport.py", label="Enter New Report")
st.sidebar.page_link("pages/02_FBReportSearch.py", label="Feedback Report Search")
st.sidebar.page_link("pages/03_ReportDL.py", label="Feedback Report Download")
st.sidebar.page_link("pages/04_GuidelinesPage.py", label="Guidelines Page")

if st.sidebar.button("Logout", type="tertiary"):
    logout()

# Page Proper
st.title("Mey Han Feedback Program")
st.header("Enter New Report")

with st.form("Event Details"):
    st.subheader("Event Information")
    with st.expander("**Event Details**", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            Event_ID = st.text_input("**Event ID**")
        with col2:
            Event_Date = st.date_input("**Event Date**")
        with col3:
            Event_Time = st.time_input("**Event Time**")

        col1, col2 = st.columns(2)
        with col1:
            Client_Name = st.text_input("**Client Name**")
        with col2:
            Event_Address = st.text_input("**Event Address**")
        Inspector_Name = st.text_input("**Inspector Name**")

    with st.expander("**Event Images**"):
        tab1, tab2, tab3, tab4 = st.tabs([
            "**Buffet Setup Photo**",
            "**Table Setup Photo**",
            "**Onsite Venue Photo**",
            "**Onsite Staff Photo**"
        ])
        with tab1:
            st.write("**Buffet Setup Photo**")
            buffet_photo = st.file_uploader("Please upload a clear photo of the buffet setup",
                                            type=["png", "jpg", "jpeg"])
        with tab2:
            st.write("**Table Setup Photo**")
            table_photo = st.file_uploader("Please upload a clear photo of the table setup",
                                           type=["png", "jpg", "jpeg"])
        with tab3:
            st.write("**Onsite Venue Photo**")
            onsite_photo = st.file_uploader("Please upload a clear photo of the entire venue setup.",
                                            type=["png", "jpg", "jpeg"])
        with tab4:
            st.write("**Onsite Staff Photo**")
            staff_group_photo = st.file_uploader("Please upload a clear group photo of the onsite staff.",
                                                 type=["png", "jpg", "jpeg"])

    st.subheader("Feedback Report")
    with st.expander("**Buffet Setup**"):
        BS1 = st.radio("Is the buffet covered in a clean skirting cloth free of holes and stains?", ["Yes", "No"])
        BSR1 = st.text_area("Remarks", key="BSR1")

        BS2 = st.radio("Is the buffet skirting cloth properly and cleanly pinned and pleated?", ["Yes", "No"])
        BSR2 = st.text_area("Remarks", key="BSR2")

        BS3 = st.radio(
            "Does each dish on the buffet have a clean serving spoon and banana boat placed beside the warmer? ",
            ["Yes", "No"])
        BSR3 = st.text_area("Remarks", key="BSR3")

        BS4 = st.radio("Does each buffet dish have a properly lit burner and underliner installed under each warmer? ?",
                       ["Yes", "No"])
        BSR4 = st.text_area("Remarks", key="BSR4")

        BS5 = st.radio("Is each dish served on the buffet presented in a satisfactory manner? ", ["Yes", "No"])
        BSR5 = st.text_area("Remarks", key="BSR5")

        BS6 = st.radio(
            "Does the buffet have a buffet flower properly displayed at the middle/corner of the buffet table? ",
            ["Yes", "No"])
        BSR6 = st.text_area("Remarks", key="BSR6")

        BS7 = st.radio(
            "Does the buffet table have its respective utensil basket displayed and appropriately stocked with tissues and alcohol? ",
            ["Yes", "No"])
        BSR7 = st.text_area("Remarks", key="BSR7")

        BS8 = st.radio(
            "Are the utensils placed atop a clean cloth and serving tray and not directly on the buffet table? ",
            ["Yes", "No"])
        BSR8 = st.text_area("Remarks", key="BSR8")

        BS9 = st.radio("Is the Mey Han Contact List Stand displayed alongside the buffet flower?", ["Yes", "No"])
        BSR9 = st.text_area("Remarks", key="BSR9")

    with st.expander("**Table Setup**"):
        TS1 = st.radio("Are all designated ruby chairs properly covered with a clean, white seat cover? ",
                       ["Yes", "No"])
        TSR1 = st.text_area("Remarks", key="TSR1")

        TS2 = st.radio(
            "Are all tables completely covered with a clean and presentable tablecloth, top cloth and runner? ",
            ["Yes", "No"])
        TSR2 = st.text_area("Remarks", key="TSR2")

        TS3 = st.radio(
            "Do all tables have a presentable table arrangement displayed at the center of each round table? ",
            ["Yes", "No"])
        TSR3 = st.text_area("Remarks", key="TSR3")

        TS4 = st.radio("Are all used seat covers, tablecloths and top cloths free of holes and stains? ", ["Yes", "No"])
        TSR4 = st.text_area("Remarks", key="TSR4")

    with st.expander("**Server Inspection**"):
        SI1 = st.radio(
            "Are all wait staff wearing complete uniform consisting of a black necktie, red long-sleeved polo shirt, black pants and black dress shoes?",
            ["Yes", "No"])
        SIR1 = st.text_area("Remarks", key="SIR1")

        SI2 = st.radio("Do all wait staff have their shirts properly tucked in?", ["Yes", "No"])
        SIR2 = st.text_area("Remarks", key="SIR2")

        SI3 = st.radio("Are all wait staff properly groomed with presentable haircut?", ["Yes", "No"])
        SIR3 = st.text_area("Remarks", key="SIR3")

        SI4 = st.radio("Are all wait staff wearing clean and presentable uniform?", ["Yes", "No"])
        SIR4 = st.text_area("Remarks", key="SIR4")

        SI5 = st.radio(
            "(Monitor over a prolonged period): Are all wait staff actively working during the event by attending to and serving customers? ",
            ["Yes", "No"])
        SIR5 = st.text_area("Remarks", key="SIR5")

    submission = st.form_submit_button("**SUBMIT REPORT**", use_container_width=True)

if submission:
    if not Event_ID.strip():
        st.error("⚠️ **Event ID is required** to submit the feedback report.")
    else:
        event_data = {
            "Event_ID": Event_ID,
            "Client_Name": Client_Name,
            "Event_Date": str(Event_Date),
            "Event_Time": str(Event_Time),
            "Inspector_Name": Inspector_Name,
            "Event_Address": Event_Address,
        }

        feedback_data = {
            "BS1": BS1, "BS2": BS2, "BS3": BS3, "BS4": BS4, "BS5": BS5, "BS6": BS6, "BS7": BS7, "BS8": BS8, "BS9": BS9,
            "TS1": TS1, "TS2": TS2, "TS3": TS3, "TS4": TS4,
            "SI1": SI1, "SI2": SI2, "SI3": SI3, "SI4": SI4, "SI5": SI5,
            "BSR1": BSR1, "BSR2": BSR2, "BSR3": BSR3, "BSR4": BSR4, "BSR5": BSR5, "BSR6": BSR6, "BSR7": BSR7,
            "BSR8": BSR8, "BSR9": BSR9,
            "TSR1": TSR1, "TSR2": TSR2, "TSR3": TSR3, "TSR4": TSR4,
            "SIR1": SIR1, "SIR2": SIR2, "SIR3": SIR3, "SIR4": SIR4, "SIR5": SIR5
        }

        # Handle Image Uploads to Supabase Storage
        image_urls = {"Event_ID": Event_ID}
        photos_to_upload = {
            "Buffet_Setup_Photo": buffet_photo,
            "Table_Setup_Photo": table_photo,
            "Onsite_Photo": onsite_photo,
            "Staff_Group_Photo": staff_group_photo
        }

        for column_name, file_object in photos_to_upload.items():
            if file_object is not None:
                file_extension = file_object.name.split(".")[-1]
                storage_path = f"{Event_ID}/{column_name}.{file_extension}"
                file_bytes = file_object.getvalue()

                supabase.storage.from_("Event_Images").upload(
                    path=storage_path,
                    file=file_bytes,
                    file_options={
                        "content-type": f"image/{file_extension}",
                        "upsert": "true"
                    }
                )

                public_url = supabase.storage.from_("Event_Images").get_public_url(storage_path)
                image_urls[column_name] = public_url
            else:
                image_urls[column_name] = None

        try:
            # 1. Save to Supabase database
            supabase.table("event_details").insert(event_data).execute()
            supabase.table("event_feedback").insert(feedback_data).execute()
            supabase.table("event_image_table").insert(image_urls).execute()

            # 2. Store data in session state so download persists after submit
            st.session_state.report_generated = True
            st.session_state.template_context = {**event_data, **feedback_data}

            st.success('🎉 Feedback Report Saved Successfully!')

        except Exception as e:
            st.error(f"❌ Failed to save data to database: {e}")

# If the report was successfully submitted, display the document download button
if st.session_state.get("report_generated", False):
    st.divider()
    st.subheader("📥 Download Generated Report")

    try:
        # Load your template file 'Inspection_Document.docx' from the project folder
        doc = DocxTemplate("Inspection_Document.docx")
        doc.render(st.session_state.template_context)

        doc_io = io.BytesIO()
        doc.save(doc_io)
        doc_io.seek(0)

        # Get the client name from session state and clean it for a safe file name
        client_name = st.session_state.template_context.get("Client_Name", "Client")
        safe_client_name = "".join(
            c if c.isalnum() or c in (' ', '_', '-') else '_' for c in client_name).strip().replace(' ', '_')

        # Fallback if the user left Client Name blank
        if not safe_client_name:
            safe_client_name = "Inspection_Report"
        else:
            safe_client_name = f"Inspection_Report_{safe_client_name}"

        st.download_button(
            label=f"📄 Click Here to Download {client_name}'s Report (.docx)",
            data=doc_io,
            file_name=f"{safe_client_name}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            type="primary",
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Could not load 'Inspection_Document.docx' template from folder: {e}")