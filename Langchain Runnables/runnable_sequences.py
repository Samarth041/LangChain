from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()

#normal
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"topic":"AI"}))