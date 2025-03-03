#imports
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

#prompt

prompt = ChatPromptTemplate.from_messages([
    ("system","listen to whatever user says"),
    ("user","write song lyrics for the theme on the theme{theme} in and around 200 words and do not respond to any other questions")

])

#LLM

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = "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",
    temperature = 0
)

#output

op = StrOutputParser()

#chain

chain = prompt | llm | op

#streamlit

st.title("THEME BASED LYRIC GENERATOR")
input_text = st.text_input("ENTER YOUR THEME")
output = chain.invoke({"theme":input_text})
st.write(output)

