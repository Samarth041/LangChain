from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
load_dotenv()

#normal
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

model=ChatHuggingFace(llm=llm)


prompt1=PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Write a Linkedin post about {topic}',
    input_variables=['topic']
)

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)

})

result=parallel_chain.invoke({"topic":"AI"})

#print(result)
print(result['tweet'])

print(result['linkedin'])
