#Author: Keith E. Coggin (Outdor/Outdor79)
#Company: Boot.Dev
#Project: AIAgent (Unit 8: Build an AI Agent)
#Project Date: 2026/08/05
#Summary: Building a toy version of Claude Code.

### IMPORTS ###
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load dotenv.
load_dotenv()

# Load API Key.
try:
    api_key = os.environ.get("OPENROUTER_API_KEY")
except:
   raise RuntimeError("API Key not found")


# Point OpenAI at the OpenRouter url.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Use the client.chat.completions.create() method to get a response from the model.
model = "openrouter/free"
messages = [
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]
response = client.chat.completions.create(model=model, messages=messages)

### MAIN ###
def main():
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
