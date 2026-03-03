 #integration package between langchain and open ai
from langchain_openai import OpenAI
#loads the secret key/ env details from .env file to current file
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model ='gpt-3.5-turbo-instruct')
# input as string output as string
result = llm.invoke("What is the capital of India")

print(result)
#optput:Capital of india is Delhi

##llms are old now chatmodels are used