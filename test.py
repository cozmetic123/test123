import streamlit as st
import os
from datetime import datetime

# Streamlit UI
st.title("Save and Download Text File")
st.write("Enter some text below and click 'Save' to generate a downloadable file.")

# Text input box
user_input = st.text_area("Enter your text here:")

# Button to save the text
if st.button("Save"):
    # Define the filename with a timestamp to avoid overwriting
    filename = f"user_input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Save the text to a file
    with open(filename, "w") as file:
        file.write(user_input)
    
    st.success(f"Text has been saved as {filename}.")

    # Provide a download button
    with open(filename, "r") as file:
        st.download_button(
            label="Download Text File",
            data=file,
            file_name=filename,
            mime="text/plain"
        )
