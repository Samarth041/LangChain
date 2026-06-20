from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#normal
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

model=ChatHuggingFace(llm=llm)

#1st template

template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

#2nd prompt
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1=template1.invoke({"topic":"black hole"})

result=model.invoke(prompt1)

prompt2=template2.invoke({"text":result.content})

result1=model.invoke(prompt2)

print(result1.content)

#without output parser we have to extract the text from result and then we can send in prompt 2