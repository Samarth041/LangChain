from dotenv import load_dotenv
import os
from google import genai

# load .env file
load_dotenv()

# get API key
api_key = os.getenv("GOOGLE_API_KEY")

# create client
client = genai.Client(api_key=api_key)

# list models
models = client.models.list()

for m in models:
    print(m.name)