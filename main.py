#Author: Keith E. Coggin (Outdor/Outdor79)
#Company: Boot.Dev
#Project: AIAgent (Unit 8: Build an AI Agent)
#Project Date: 2026/08/05
#Summary: Building a toy version of Claude Code.

### IMPORTS ###
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI


### MAIN ###
def main():
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


    # Create a parser object and parse th euser input.
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`


    # Define the OpenRouter model to use.
    model = "openrouter/free"

    # Create a list of messages,
    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    # Use the client.chat.completions.create() method to get a response from the model.
    response = client.chat.completions.create(model=model, messages=messages)

    # Ouput response to the user if one is recieved atherwise raise an error.
    if response is not None:
        # If user has requested verbose responses include the Ptompt and token counts.
        if args.verbose is True:
            print(f"User prompt: {messages[0]['content']}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        # Print the response either way.
        print("Response:")
        print(response.choices[0].message.content)
    else:
        raise RuntimeError("invalid server response")

if __name__ == "__main__":
    main()
