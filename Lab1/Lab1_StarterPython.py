import openai
import os

# Initialize the OpenAI client with the API key from the environment
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create a chat completion request
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a expert in Machine Learning."},
        {"role": "user", "content": "Explain the concept of transformers in machine learning."}
    ]
)

# Print the response
print(completion.choices[0].message.content)