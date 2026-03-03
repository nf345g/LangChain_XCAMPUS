from langchain_huggingface import ChatHuggingFace, HuggingFacepipeline
from dotenv import load_dotenv

load_dotenv()

#downling in the systme by default in c drive
#to change the location of the docmload model
os.environ['HF_HOME'] ='D:/huggingface_cache'
#if the model is already downloded it will not downlaod onceagain only first run it will download
#next time when you run it will take the cached version
llm = HuggingFacepipeline.from_model_id( 
    #downloading the model... it takes lots of time to run the model,
    # we require goog configuration in local system
    model_id ="TinyLlama/TinyLlama-1.18-chat-v1.0", 
    task ="text-generation",
    pipeline_kwargs = dict(temperature = 0.5, max_new_tokens=100
    )
    )

model = ChatHuggingFace(llm=llm)
model.invoke("What is the capital of India")

#optput: output in json format with parameters like content, meta data,content
print(result)

print(result.content)
#optput:Capital of india is Delhi


