from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")

paper_input = st.selectbox("Select research paper name", ["Select....", "Attention is all you need", 
"Bert:Pre training of deep bidirectional transformers", "GPT-3 models are few-shot learners", 
 "Diffusion model beat GANs on image synthesis"])

style_input = st.selectbox("Select explanation style", ["Select....", "Beginner friendly", 
 "Technical", "code oriented", 
 "Mathematical"])

length_input = st.selectbox("Select explanation length", ["Select....", "short 1-2 paragraph", 
 "medium 3-5 paragraph", "Long (detailed explanation)"])

template = PromptTemplate(
    template ="""
    please summarize the research paper titled "{paper_input}" with thre following specifications:
    Explanation style : {style_input}
    Explanationlength: {length_input}
    1. Mathematical details:
        - include relevant mathematical equation if present in the paper.
        - include the mathematical concept using simple, intutive code snippets where applicable.
    2. Analogies:
        - Use relateble analogies to simplify complex ideas
    If information is not available in paper, respond with: "Insufficient information available" instead of guessing.
    
    Ensure the summary is clear accurate and aligned with the provided style and length"""
    , input_variables = ['paper_input','style_input','length_input']
)

prompt = template.invoke({'paper_input':paper_input,
                 'style_input':style_input,
                 'length_input':length_input
                 })

if st.button('summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
    #st.write("abc")