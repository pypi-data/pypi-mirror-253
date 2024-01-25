# aiKnow

<p align="center">
  <img 
    src="./resources/aiknow-logo-light.jpg" 
    width="50%"
  />
</p>

A framework of utilizing LLM agents. 

## Installation

Clone this repository:

```bash
git clone https://github.com/midnight-learners/aiknow.git
```

Navigate to the root directory of the repository and install the dependencies:

```bash
poetry install
```

## Chat Models

### Models

Currently, we support chat models from both OpenAI and Qianfan.


```python
from aiknow.llm import OpenAIChatModel, QianfanChatModel
```

### Authentication

Create a `.env` file in the root directory of your project, and fill in the following fields:

```bash
# OpenAI
OPENAI_API_KEY = ""

# Qianfan
QIANFAN_ACCESS_KEY = ""
QIANFAN_SECRET_KEY = ""
```

Our chat models will automatically load the authentication information from this `.env` file.


```python
# Create a chat model
chat_model = OpenAIChatModel(
    name="gpt-3.5-turbo",
    temperature=0.9,
)
```

### Getting Chat Responses

Call the API and get a complete response:


```python
chat_model.get_complete_response("Hello?")
```




    ChatResponse(content='Hi there! How can I assist you today?', token_usage=ChatTokenUsage(prompt_tokens=9, completion_tokens=10, total_tokens=19))



Get a streamed response:


```python
for response in chat_model.get_streamed_response("What is AI?"):
    print(response.content, end="", flush=True)
```

    AI, short for Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. It involves the development of computer systems capable of performing tasks that normally require human intelligence, such as speech recognition, decision-making, problem-solving, visual perception, and language translation. AI can be classified into two types: Narrow AI, which is designed for specific tasks, and General AI, which exhibits human-like intelligence and can perform any intellectual task that a human being can do.

We also support async calls.

Get a complete response asynchronously:


```python
await chat_model.get_complete_response_async("Hello?")
```




    ChatResponse(content='Hello! How can I assist you today?', token_usage=ChatTokenUsage(prompt_tokens=9, completion_tokens=9, total_tokens=18))



Get a streamed response asynchronously:


```python
async for response in await chat_model.get_streamed_response_async("What is AI?"):
    print(response.content, end="", flush=True)
```

    AI, or Artificial Intelligence, refers to the development of computer systems that can perform tasks that typically require human intelligence. These systems are designed to mimic human thought processes, analyze data, learn from experiences, and make decisions or take actions based on that analysis. AI aims to automate and enhance various aspects of human life and work, such as speech recognition, problem-solving, decision-making, learning, and visual perception, among others. AI technologies include machine learning, natural language processing, computer vision, robotics, and more.
