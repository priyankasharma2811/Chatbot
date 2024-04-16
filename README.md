=# LLM-Powered Agent

## Project Overview

This project develops an LLM (Large Language Model) powered agent designed to answer natural language questions. Utilizing advanced language processing technologies, the agent demonstrates basic conversational capabilities through a web interface. The primary focus is on configurability, scalability, design and accuracy of responses.

### Key Features

- Natural language question answering
- Web interface for enhanced user interaction
- Configurable and scalable design suitable for future enhancements

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Access to an LLM API (e.g., Amazon bedrock)

### Installation

Clone the repository:

```
git clone https://github.com/priyankasharma2811/Chatbot.git
cd Chatbot
```

Install the required dependencies:

```
pip install -r requirements.txt
```
## Environment Setup

To run the chatbot, you need to set the following environment variables:

- `LLM_MODEL_ID`: The model identifier for the LLM. Example: 'meta.llama2-13b-chat-v1'
- `LLM_TEMPERATURE`: Controls the randomness of the response generation. Example: 0.9
- `LLM_TOP_P`: Controls the nucleus sampling. Example: 0.5
- `LLM_MAX_GEN_LEN`: Maximum generation length of the responses. Example: 512
- `AWS_REGION`: The AWS region where the services are deployed. Example: 'us-east-1'

These variables can be set in an `.env` file located in the root directory of the project.

### Setup

- Obtain API keys for the chosen LLM service.
- Configure the application with your API keys and preferred settings.

## Usage

Run the backend file:

```
python backend.py
```

For the web interface:

```
python frontend.py
```

### Examples

```
> python frontend.py
> Ask me anything: How does the LLM-powered agent work?
> The LLM-powered agent processes your question and uses a language model to generate a response.
