from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model ='claude-3-5-sonnet-20241022')
# input as string output as string
result = llm.invoke("What is the capital of India")
result = llm.invoke("What is the capital of India",temperate=0)#0-2
result = llm.invoke("What is the capital of India",temperate=0,max_completion_tokens=10)

#optput: output in json format with parameters like content, meta data,content
print(result)

print(result.content)
#optput:Capital of india is Delhi


