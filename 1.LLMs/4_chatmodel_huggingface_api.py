from langchain_huggingface import ChatHuggingFace, HuggingFaceEndPoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndPoint(
    repo_id ="TinyLlama/TinyLlama-1.18-chat-v1.0", 
    task ="text-generation")

model = ChatHuggingFace(llm=llm)
model.invoke("What is the capital of India")
# input as string output as string
result = llm.invoke("What is the capital of India")
result = llm.invoke("What is the capital of India",temperate=0)#0-2
result = llm.invoke("What is the capital of India",temperate=0,max_completion_tokens=10)

#optput: output in json format with parameters like content, meta data,content
print(result)

print(result.content)
#optput:Capital of india is Delhi


