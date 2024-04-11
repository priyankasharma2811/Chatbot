import os
from dotenv import load_dotenv
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()

# Configurable parameters
model_id = os.getenv('LLM_MODEL_ID', 'meta.llama2-13b-chat-v1')
temperature = float(os.getenv('LLM_TEMPERATURE', '0.9'))
top_p = float(os.getenv('LLM_TOP_P', '0.5'))
max_gen_len = int(os.getenv('LLM_MAX_GEN_LEN', '300'))
region_name = os.getenv('AWS_REGION', 'us-east-1')

# Initialization
# This section sets up the language model (LLM) environment and configuration.

def demo_chatbot():
    # Model Setup
    # Create a Bedrock LLM instance with specific model parameters.
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id=model_id,
        model_kwargs={
            "temperature": temperature,
            "top_p": top_p,
            "max_gen_len": max_gen_len 
        },
        region_name=region_name  
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

    # Example of dynamic response length adjustment
    if 'explain' in input_text or 'detail' in input_text:
        # If the user asks for an explanation or detail, return a longer response
        sentences = full_response.split('.')
        response = '. '.join(sentences[:3])  # Adjust number of sentences as needed
    else:
        # For other types of queries, return a shorter response
        sentences = full_response.split('.')
        response = sentences[0] if sentences else full_response

    return response.strip() + ('.' if not response.endswith('.') else '')



