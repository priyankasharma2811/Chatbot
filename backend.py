import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Initialization
# This section sets up the language model (LLM) environment and configuration.

def demo_chatbot():
    # Model Setup
    # Create a Bedrock LLM instance with specific model parameters.
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id='meta.llama2-13b-chat-v1',
        model_kwargs={
            "temperature": 0.9,
            "top_p": 0.5,
            "max_gen_len": 300 
        },
        region_name='us-east-1'  
    )
    return demo_llm

# Memory Management
# Setup conversation memory to retain context in a chat session.
def demo_memory():
    llm_instance = demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_instance, max_token_limit=512)
    return memory

# API Functions
# Define any additional functions that will interface with the front end.
def demo_conversation(input_text, memory): 
    llm_instance = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_instance, memory=memory, verbose=True)
    full_response = llm_conversation.run({'input': input_text})
    trimmed_response = full_response.split('.')[0] + '.'  # Split by period for sentences
    return trimmed_response



