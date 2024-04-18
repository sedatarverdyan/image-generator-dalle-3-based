
import streamlit as st

# Initialize session state for chat messages
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

st.title("Image Generator")

# Function to update chat messages
def update_chat_messages(message):
    st.session_state.chat_messages.append(message)

with st.chat_message("assistant"):
    st.write("Let's generate a picture together!")
    prompt = st.chat_input("Describe a picture")
    if prompt:
        update_chat_messages(("user", prompt))

# Display chat messages
for role, message in st.session_state.chat_messages:
    with st.chat_message(role):
        st.write(message)

option1 = st.selectbox(
    label="Select style",
    options=("Van Gogh Style","Cartoon Style","Sketch Style","Watercolor Style",
             "Impressionist Style","Pop Art Style","Realistic Oil Painting Style",
             "Minimalist Style","Surrealism Style","Pointillism Style","Fauvism Style")
)

option2 = st.selectbox(
    label="Select size",
    options=("256x256 pixels","128x128 pixels","64x64 pixels","Custom Size")
)

if st.button("Generate"):
    # Perform image generation based on user input and selected options
    # Add your image generation code here
    st.write("Image generated!")
