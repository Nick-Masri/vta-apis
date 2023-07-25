import streamlit as st
from calls.chargepoint import chargepoint_active_sessions, chargepoint_past_sessions, chargepoint_stations, financial_transaction_data
st.write("# Welcome to the Chargepoint page!")

# selectbox for calls on the center
selected = st.sidebar.selectbox("Select a call", ["Get Stations", "Get Active Sessions", "Get Past Sessions", "Get Transaction Data"])

def formify(call, text):
    with st.form(key=text):
        st.write(f"## {text}")
        if text == "Get Past Sessions":
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            submit_button = st.form_submit_button(label="Submit")
            if submit_button:
                st.write(call(start_date, end_date))
        else:
            submit_button = st.form_submit_button(label="Submit")
            if submit_button:
                st.write(call)

        
if selected == "Get Stations":
    formify(chargepoint_stations(), "Get Stations")
elif selected == "Get Active Sessions":
    formify(chargepoint_active_sessions(), "Get Active Sessions")
elif selected == "Get Past Sessions":
    formify(chargepoint_past_sessions, "Get Past Sessions")
elif selected == "Get Transaction Data":
    st.write("Unable to access. Need a chargepoint enterprise account.")
    # formify(financial_transaction_data(), "Get Financial Transaction Data")
