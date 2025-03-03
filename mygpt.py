#imports

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#code

#prompt

prompt1 = ChatPromptTemplate.from_messages([
    ("system","listen to whatever user says"),
    ("user","give a precise answer to the question{question}")

])

#LLM

#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

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key= "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",
    temperature = 0
)

#output

op = StrOutputParser()


#chain
chain = prompt1 | llm | op

#streamlit
st.title("MY GPT")
input_text = st.text_input("Enter the question")
output = chain.invoke({"question":input_text})
st.write(output)