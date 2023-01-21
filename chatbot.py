import random
import nltk

# List of responses
responses = [
    "Hello!",
    "Hi there!",
    "How are you?",
    "I'm doing well, thanks for asking.",
    "What's your name?",
    "My name is Chatbot. Nice to meet you!",
]

# Greet the user
print(random.choice(responses))

# Get the user's input
message = input("What's your name? ")

# Respond to the user's message
print(f"Hi, {message}! It's nice to meet you.")

# Continuously get user input and respond
while True:
    # Get the user's input
    message = input("What can I help you with today? ")

    # Use NLTK to tokenize the message and tag the part of speech of each word
    tokens = nltk.word_tokenize(message)
    pos_tags = nltk.pos_tag(tokens)

    # Use NLTK to recognize named entities in the message
    named_entities = nltk.ne_chunk(pos_tags)

    # If the message contains a greeting, respond with a random greeting
    if "hello" in tokens or "hi" in tokens:
        print(random.choice(responses))
    # If the message contains a question, respond with a question
    elif "?" in message:
        print("I'm sorry, I'm not able to answer questions at this time.")
    # If the message contains a farewell, respond with a farewell
    elif "goodbye" in tokens or "bye" in tokens:
        print("Goodbye! It was nice chatting with you.")
        break
    # If the message contains a request for the weather, respond with the weather
    elif "weather" in tokens:
        print("I'm sorry, I'm not able to provide weather information at this time.")
    # If the message contains a verb in the past tense, respond with a past tense verb
    elif any(tag in ["VBD", "VBN"] for (word, tag) in pos_tags):
        print("I'm sorry, I'm not able to process past tense verbs at this time.")
    # If the message contains a named entity of type "PERSON", respond with a personalized greeting
    else:
        for entity in named_entities:
            if isinstance(entity, nltk.tree.Tree):
                if entity.label() == "PERSON":
                    name = " ".join(word for word, tag in entity.leaves())
                    print(f"Hi, {name}! It's nice to meet you.")
                    break
        else:
            print(random.choice(responses))
