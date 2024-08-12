import streamlit as st
import os
from datetime import datetime

# Define the directory where you want to save the file
save_directory = "E:\\University\\Code\\ticTac\\"

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Streamlit UI
st.title("Save Text to Local File")
st.write("Enter some text below and click 'Save' to store it in a file on your local computer.")

# Text input box
user_input = st.text_area("Enter your text here:")

# Button to save the text
if st.button("Save"):
    # Define the filename with a timestamp to avoid overwriting
    filename = f"user_input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Combine the directory with the filename
    file_path = os.path.join(save_directory, filename)
    
    # Save the text to the file
    with open(file_path, "w") as file:
        file.write(user_input)
    
    st.success(f"Text has been saved to {file_path} on your local computer.")
