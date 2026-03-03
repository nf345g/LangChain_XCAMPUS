from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human','{query}')
])

chat_hist =[]
#load chat history
with open('chatHistory.txt') as f:
    chat_hist.extend(f.readlines())

print(chat_hist)

#create prompt
prompt = chat_template.invoke({'chat_history':chat_hist, 'query': 'Where is my refund'})

print(prompt)