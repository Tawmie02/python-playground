import random

# Responses
greetings = ["Hey!", "Hello!", "Hi there!", "Yo!"]
farewells = ["Bye!", "See you!", "Catch you later!"]

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(greetings)
    elif "how are you" in user_input:
        return "I'm code, but I'm running great! "
    elif "python" in user_input:
        return "Python is awesome! Are you working on a project?"
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "AI is cool! You can build a chatbot like me "
    elif "bye" in user_input:
        return random.choice(farewells)
    else:
        return "Hmm... I don't know about that yet."

def save_chat(user, bot):
    with open("chat.txt", "a") as file:
        file.write(f"You: {user}\nBot: {bot}\n\n")

# Main loop
print("Smart Chatbot: Hello! I'm your CS buddy. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Smart Chatbot:", response)
    save_chat(user_input, response)

    if "bye" in user_input.lower():
        break