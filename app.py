import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core import output_parsers
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#prompt
prompt=ChatPromptTemplate(
  [
    ("system", "You are a helpful assistance. Please respond to the question asked."),
    ("user", "Question:{question}")
  ])

#streamlit
st.title("Langchain Demo with Llama 3 - Open Source")
input_text=st.text_input("Ask any question!")

#call model
llm=Ollama(model="llama3")

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
  st.write(chain.invoke({"question":input_text}))


















