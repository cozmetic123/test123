import streamlit as st

print("Streamlit app started")  # Check if the app is launching

# Streamlit UI
st.title("Save Text to File")
st.write("Enter some text below and click 'Save' to store it in a file.")

user_input = st.text_area("Enter your text here:")

if st.button("Save"):
    print("Save button pressed")  # Check if the button press is detected
    filename = "user_input.txt"
    with open(filename, "w") as file:
        file.write(user_input)
    st.success(f"Text has been saved to {filename}")
