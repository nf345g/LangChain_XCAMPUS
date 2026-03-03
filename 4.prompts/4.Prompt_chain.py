from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")

paper_input = st.selectbox("Select research paper name", 
                            ["Select...."
                             , "Attention is all you need"
                             , "Bert:Pre training of deep bidirectional transformers"
                             , "GPT-3 models are few-shot learners"
                             , "Diffusion model beat GANs on image synthesis"
                             ]
                           )

style_input = st.selectbox("Select explanation style"
                            , ["Select...."
                                , "Beginner friendly"
                                , "Technical", "code oriented"
                                , "Mathematical"
                              ]
                          )

length_input = st.selectbox("Select explanation length", ["Select....", "short 1-2 paragraph", 
 "medium 3-5 paragraph", "Long (detailed explanation)"])

template = load_prompt('template.json')

if st.button('summarize'):
    chain = template | model
    result = chain.invoke({'paper_input':paper_input,
                            'style_input':style_input,
                            'length_input':length_input
                            })
    st.write(result.content)

# here we are calling invoke 2 times. 
#1. to invoke templpate
#2. to invoke model

#so instaed of calling invoke 2 times on template and model 
#you can use chains invoke
   