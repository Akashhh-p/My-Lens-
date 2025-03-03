import google.generativeai as genai
import streamlit as st


#get api key

genai.configure(api_key="AIzaSyBqe7iRP0HqFZrHRInm-osnjes0e8cHQqs")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def get_response(input_question):
    response = model.generate_content(input_question)
    return response.text

#streamlit
st.title("MY GEMINI GPT")
input = st.text_input("enter question")
button = st.button("click me")
if button:
    output = get_response(input)
    st.write(output)