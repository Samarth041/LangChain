from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

#normal
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me 5 facts about {topic} \n  \n{format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


#prompt=template.format() 
#print(prompt)--this will print something like "Give me the name,age and city of a fictioanal person 
#Return a JSON object."


chain=template | model | parser
result=chain.invoke({"topic":"black hole"})

print(result)




