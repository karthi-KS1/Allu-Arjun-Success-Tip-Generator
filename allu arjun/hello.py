import tips

import random

# List of possible bot responses
greetings = [
    "Hello! How are you today?",
    "Hi there! What's new?",
    "Hey! How's it going?",
    "Greetings! How can I assist you?",
    "Hi! Tell me, how can I make your day better?"
]

farewells = [
    "Goodbye! Take care.",
    "Farewell! Have a great day!",
    "Until next time! Stay awesome.",
    "Bye! Remember, I'm always here for a chat.",
    "Take care! It was nice talking to you."
]

positive_emotions = [
    "That's great!",
    "I'm glad to hear that!",
    "Awesome!",
    "Fantastic!",
    "Wonderful!"
]

negative_emotions = [
    "I'm sorry to hear that.",
    "That must be tough.",
    "Hang in there. Things will get better.",
    "If you need to talk, I'm here for you.",
    "I'm sending positive vibes your way."
]

interesting_topics = [
    "Tell me more about it.",
    "That's fascinating! Could you elaborate?",
    "I'd love to hear your thoughts on that.",
    "Interesting! What inspired you to think about this?",
    "That's a great topic. Let's dive deeper into it."
]

continue_stuff = [
    "is there anything else you want to talk about?",
    "so, what else?",
    "have a great day then ig"
    ]
# Function to generate a random response from the given list
def get_response(options):
    return random.choice(options)

# Main conversation loop
def chat():
    print("Hello! I'm your friendly companion. How can I help you today?")
    while True:
        user_input = input("> ").lower()

        if user_input in ["bye", "goodbye","no"]:
            print(get_response(farewells))
            break

        elif any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            print(get_response(greetings))

        elif any(emotion in user_input for emotion in ["good", "great", "awesome", "fantastic"]):
            print(get_response(positive_emotions))

        elif any(emotion in user_input for emotion in ["bad", "not good", "terrible", "awful","sad"]):
            print(get_response(negative_emotions))
            tips.tips()

        elif any(topic in user_input for topic in ["saw a", "talk about", "discuss"]):
            print(get_response(interesting_topics))

        elif any(topic in user_input for topic in ["yes", "ok", "nice"]):
            print(get_response(continue_stuff))

        else:
            print("I'm sorry, I didn't understand. Can you rephrase or ask another question?")

# Start the conversation
chat()

