from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    max_new_tokens=512,
    temperature=0.5
)
model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input=st.text_input('Enter your prompt')

if st.button('Summarise'):
    result = model.invoke(user_input)
    st.write(result.content)