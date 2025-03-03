import google.generativeai as genai
from PIL import Image
import streamlit as st


genai.configure(api_key= "AIzaSyBqe7iRP0HqFZrHRInm-osnjes0e8cHQqs")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def get_response(image,prompt):
   response = model.generate_content([image,prompt])
   return response.text

#streamlit
st.title("MY LENS")
image = st.file_uploader("upload the image",type=["jpeg","png"])
input = st.text_input("enter the question for image")
button = st.button("click me")

#display
if button:
   im = Image.open(image)
   st.image(im)
   output = get_response(im,input)
   st.write(output)