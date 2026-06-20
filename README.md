# Basic Chatbot

## Goal
Build a simple rule-based chatbot.

## Scope
- Takes input from the user like "hello", "how are you", "bye".
- Responds with predefined replies like "Hi!", "I'm fine, thanks!", "Goodbye!".

## Key Concepts Used
- `if-elif` — to match user input to the correct response
- Functions — to organize response logic and the chat loop
- Loops — to keep the conversation running until the user exits
- Input/Output — to take user input and print bot replies

## How It Works
1. The program greets the user and starts a chat loop.
2. The user types a message.
3. The chatbot checks the message against known keywords (hello, how are you, your name, thanks, bye).
4. A matching predefined reply is randomly chosen and displayed.
5. If the input doesn't match any known pattern, a fallback "I didn't understand that" reply is shown.
6. Typing "bye" (or similar) ends the conversation.

## How to Run
```bash
python3 task4_chatbot.py
```

## Sample Conversation
You: hello

Bot: Hi!
You: how are you

Bot: I'm fine, thanks!
You: bye

Bot: Goodbye!

## File Structure
CHATBOT.PY

## Possible Future Improvements
- Use NLP (e.g., regex or simple keyword scoring) for better matching
- Add more intents (jokes, weather, help commands)
- Store conversation history to a log fileYou said: ALSO COMMIT
