import streamlit as st
import os
from datetime import datetime

# Define the shared storage for the text input and filename
if 'shared_input' not in st.session_state:
    st.session_state.shared_input = ""
if 'shared_filename' not in st.session_state:
    st.session_state.shared_filename = ""

# Streamlit UI
st.title("Collaborative Text Saver")
st.write("Enter some text below and click 'Save'. The download button will be available for all users.")

# Text input box
user_input = st.text_area("Enter your text here:")

# Button to save the text
if st.button("Save"):
    # Update the shared state with the new input
    st.session_state.shared_input = user_input
    
    # Define the filename with a timestamp to avoid overwriting
    filename = f"user_input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Save the text to a file
    with open(filename, "w") as file:
        file.write(st.session_state.shared_input)
    
    # Update the shared filename in the session state
    st.session_state.shared_filename = filename
    
    st.success(f"Text has been saved as {filename}.")

# Display the download button if there's any shared input
if st.session_state.shared_input:
    st.write(f"A file has been saved: {st.session_state.shared_filename}")
    
    with open(st.session_state.shared_filename, "r") as file:
        st.download_button(
            label="Download Text File",
            data=file,
            file_name=st.session_state.shared_filename,
            mime="text/plain"
        )
