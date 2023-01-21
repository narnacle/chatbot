# Chatbot

A simple chatbot script that uses NLTK to perform natural language processing tasks.

## Getting Started

To run this script, you will need to have Python and NLTK installed on your computer. You can install NLTK using pip:

```pip install nltk```

## Usage

To run the script, simply execute the following command in your terminal:

```python chatbot.py```

The script will greet you and ask for your name. Once it has your name, it will respond to your messages and generate relevant responses.

## Features

- Recognize and respond to greetings, questions, farewells, and requests for weather information.
- Use NLTK's `pos_tag` function to tag the part of speech of each word in the user's message, and then use that information to generate a more relevant response.
- Use NLTK's `ne_chunk` function to recognize named entities in the user's message, and then use that information to personalize the response.
- Check if the message contains a verb in the past tense, and use that to generate a response that reflects the past tense of the verb.
- Check if the message contains a named entity of a certain type, and use that information to personalize the response.

## Notes

- The script is not able to answer questions or provide weather information, it is just an example.
- The script will run indefinitely and end when the user inputs "goodbye" or "bye".
- The script will print named entities to the console, you can use that to generate more relevant responses.

## Additional Resources

- [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
- [Python](https://www.python.org/)