from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st



#web base data
 
webdata = WebBaseLoader("https://www.theskillshop.in")
data = webdata.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks = splitter.split_documents(data)

#embeddings

embeddings = CohereEmbeddings(
    model = "embed-english-v3.0",
    cohere_api_key= "9snAiGkOle1kgTRk2OSFK0r7nl4suVizVxUwBR9R",

)

#vector store

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings

)

#ret

retriever = vector_store.as_retriever()

#prompt

prompt = ChatPromptTemplate.from_template(
    """
give answers only within the context{context} and precisely according to the user question{question}
"""
)

#llm
llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key= "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",
    temperature = 0
)

#output

op = StrOutputParser()

#chain 

chain = (
    {"context":retriever,"question":RunnablePassthrough()}|
    prompt|llm|op
)


#streamlit

st.title("MY WEB RAG")
input = st.text_input("enter the question for website")
button = st.button("click me")
if button:
    output = chain.invoke(input)
    st.write(output)
