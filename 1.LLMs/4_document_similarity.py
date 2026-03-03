from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from scklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 300)


documents = [
    "Delhi is the capital of india",
    "kolkata is the capita; of west bengal"
    "Parsis is the capital of France"
]

query = 'what is the capital of india'

document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

#we get 2 dimentional lost with simolarity score [[0.66 0.23 0.33 0.12]]
scores = cosine_similarity([query_embedding],document_embeddings)[0]# now its 1 d

enumerated_score = list(enumerate(scores))
print(enumerated_score) 
#enumerate will add index
#[(0, 0.66), (1, 0.23), (2, 0.33), (3, 0.12)] 
#here we have key value ofter enumerating

#now sort based on score
asc_sorted = sorted(enumerated_score, key = lambda x:x[1]
print(asc_sorted) 
#[(3, 0.12), (1, 0.23), (2, 0.33), (0, 0.66)]

#get the highest similarity
print(asc_sorted[-1])
#[(0, 0.66)]

index, score = asc_sorted[-1]

print(query)
print(documents[index])
print("similarity scores is: ", score)


