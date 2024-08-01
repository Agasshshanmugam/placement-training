import random

responses = {
    'hi': ['Hello!', 'Hi there!', 'Hey!'],
    'how are you': ['I am fine, thank you!', 'I am doing well, thanks!', 'I am great, how about you?'],
    'bye': ['Goodbye!', 'See you later!', 'Take care!']
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I don't understand."

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    print("Bot:", chatbot_response(user_input))
