import os
from dotenv import load_dotenv
import openai




# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API credentials
api_key = os.getenv("API_KEY")
openai.api_key = api_key


model_id = 'gpt-3.5-turbo'  # or your fine-tuned model ID

# Define the training prompts
training_prompts = [
    {
        "role": "system",
        "content": "You are a helpful call center staff of the insurance company."
    },
    {
        "role": "user",
        "content": "I'd like to check my insurance policy information."
    },
    {
        "role": "assistant",
        "content": "Sure, may I know your policy number?"
    },
    {
        "role": "user",
        "content": "My policy number is XXXX."
    },
    {
        "role": "assistant",
        "content": "Thank you. Let me check the system to get your policy information."
    },
    # Add more user and assistant messages as needed
]

def generate_response(prompt):

    response = openai.ChatCompletion.create(
        model = model_id,
        messages = training_prompts + [{"role": "user", "content": prompt}], 
    )

    return response['choices'][0]['message']['content'].strip()


# Example usage
bot_response = ""
while True:
    if 'policy number' in bot_response.lower():
        policy_number = input("Please provide the policy number: ")
        user_input = "My policy number is " + policy_number
    else:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

    bot_response = generate_response(user_input)
    print("ChatBot:", bot_response)
