from langchain_core.prompts import PromptTemplate

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

template.save('template.json')
//created new file template.json

