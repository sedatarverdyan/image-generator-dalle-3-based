from openai import OpenAI
import streamlit as st

api_key = 'your-secret-key'

client = OpenAI(api_key=api_key)


st.title("Image Generator")

# Function to update chat messages
def update_chat_messages(message):
    st.session_state.chat_messages = []
    
 
st.header("Let's generate a picture together!")

prompt1=st.text_input("Describe a picture and press Enter to apply")

# Check if prompt1 is None
if prompt1:
    update_chat_messages(("user", prompt1))
    with st.chat_message("user"):
            st.write(prompt1)


option1 = st.selectbox(
    label="Select style",
    options=("None","Van Gogh Style","Cartoon Style","Sketch Style","Watercolor Style",
             "Impressionist Style","Pop Art Style","Realistic Oil Painting Style",
             "Minimalist Style","Surrealism Style","Pointillism Style","Fauvism Style")
)

option2 = st.selectbox(
    label="Select size",
    options=("1024x1024","1024x1792", "1792x1024")
)

if st.button("Generate") and prompt1 is not None:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{prompt1} Generate image with this prompt, that has a {option1}",
        size=option2,
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    st.image(image_url, caption='Generated image')
