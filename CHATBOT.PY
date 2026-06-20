"""
TASK 4: Basic Chatbot
Goal: Build a simple rule-based chatbot.
Scope: Inputs like "hello", "how are you", "bye"; predefined replies.
Key Concepts: if-elif, functions, loops, input/output
"""

import random

# Predefined replies for each recognized intent
GREETING_REPLIES = ["Hi!", "Hello there!", "Hey, how's it going?"]
WELLBEING_REPLIES = ["I'm fine, thanks!", "Doing great, thanks for asking!"]
NAME_REPLIES = ["I'm a simple Python chatbot.", "You can call me ChatBot!"]
THANKS_REPLIES = ["You're welcome!", "No problem!", "Anytime!"]
GOODBYE_REPLIES = ["Goodbye!", "See you later!", "Bye, take care!"]
UNKNOWN_REPLIES = [
    "Sorry, I didn't understand that.",
    "Can you rephrase that?",
    "I'm not sure how to respond to that.",
]


def get_response(user_input):
    text = user_input.lower().strip()

    # Check for exit keywords first
    if text in ("bye", "goodbye", "exit", "quit"):
        return random.choice(GOODBYE_REPLIES), True

    if "hello" in text or "hi" in text:
        return random.choice(GREETING_REPLIES), False
    elif "how are you" in text:
        return random.choice(WELLBEING_REPLIES), False
    elif "your name" in text or "who are you" in text:
        return random.choice(NAME_REPLIES), False
    elif "thank" in text:
        return random.choice(THANKS_REPLIES), False
    elif text == "":
        return "Please type something!", False
    else:
        return random.choice(UNKNOWN_REPLIES), False


def chat():
    print("=" * 40)
    print("Simple Rule-Based Chatbot")
    print("Type 'bye' to exit the conversation.")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")
        response, should_exit = get_response(user_input)
        print("Bot:", response)

        if should_exit:
            break


if __name__ == "__main__":
    chat()