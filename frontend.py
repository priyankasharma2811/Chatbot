import streamlit as st
import backend as bk

# Setup and Configuration
# Initialize the Streamlit app and set the page title.
st.title("Hi, This is Human like bot :sunglasses:")

# Initialize conversation memory to retain chat context.
if 'memory' not in st.session_state:
    st.session_state.memory = bk.demo_memory()

# Maintain a chat history in session state for continuous conversation context.
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])

input_text = st.chat_input("chat with bot: 🤖 💬 💬 💬 💬 💬 💬 💬 💬 💬 💬 💬 ")  # Get user input.


if input_text:
    # Display the user's input in the chat.
    with st.chat_message("user"):
        st.markdown(input_text)

    # Update chat history with user's input.
    st.session_state.chat_history.append({'role': 'user', 'text': input_text})

    # Get the response from the backend using the input text and memory.
    bot_response = bk.demo_conversation(input_text, st.session_state.memory)

    # Display the bot's response in the chat.
    with st.chat_message("bot"):
        st.markdown(bot_response)

    # Update chat history with bot's response.
    st.session_state.chat_history.append({'role': 'bot', 'text': bot_response})

