from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding = HuggingFaceEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of india",


result = embedding.embed_query(text)

print(str(result)) #this oupt has vector which means the contextual meaning of the text

documents = [
    "Delhi is the capital of india",
    "kolkata is the capita; of west bengal"
    "Parsis is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result)) 

