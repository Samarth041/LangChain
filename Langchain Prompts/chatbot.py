from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    result = model.invoke(user_input)
    print("AI:", result.content)