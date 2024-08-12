import streamlit as st
import os
from datetime import datetime

# Streamlit UI
st.title("Save Text to Local File")
st.write("Enter some text below and click 'Save' to store it in a file on your local computer.")

# Text input box
user_input = st.text_area("Enter your text here:")

# Button to save the text
if st.button("Save"):
    # Define the filename with a timestamp to avoid overwriting
    filename = f"user_input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Define the local path where you want to save the file
    # You can specify an absolute path or a relative path
    # Example of saving to the current directory
    file_path = os.path.join(os.getcwd(), filename)
    
    # Save the text to the file
    with open(file_path, "w") as file:
        file.write(user_input)
    
    st.success(f"Text has been saved to {file_path} on your local computer.")

