import openai
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key
openai.api_key = api_key

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ],
    temperature=0.7,
    max_tokens=150
)


# Print the AI's response
print(response['choices'][0]['message']['content'])
