from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage


#to create dynamic messages
chat_template=ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])
prompt=chat_template.invoke({'domain':'cricket','topic':'wide'})


print(prompt)
