from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# UI
# -----------------------------

st.title("🤖 Funny AI Chatbot")
st.write("Chat with your Mistral AI agent.")


# -----------------------------
# Personality
# -----------------------------

st.subheader("Choose AI Personality")

personality = st.radio(
    "Select a personality:",
    [
        "Funny",
        "Friendly",
        "Professional"
    ],
    horizontal=True
)


# -----------------------------
# System Message
# -----------------------------

if personality == "Funny":

    system_prompt = "You are a funny ai agent."

elif personality == "Friendly":

    system_prompt = "You are a friendly ai agent."

else:

    system_prompt = "You are a professional ai agent."


# -----------------------------
# Model
# -----------------------------

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)


# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(
            content=system_prompt
        )
    ]


# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    if isinstance(message, SystemMessage):
        continue

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# -----------------------------
# User Input
# -----------------------------

prompt = st.chat_input(
    "Type your message..."
)


if prompt:

    # Add user's message
    user_message = HumanMessage(
        content=prompt
    )

    st.session_state.messages.append(
        user_message
    )


    # Display user's message
    with st.chat_message("user"):
        st.write(prompt)


    # Get AI response
    response = model.invoke(
        st.session_state.messages
    )


    # Add AI response
    ai_message = AIMessage(
        content=response.content
    )

    st.session_state.messages.append(
        ai_message
    )


    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.content)