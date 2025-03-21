import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.chat_history import AIMessage, HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Load API Key
load_dotenv()
# groq_api = os.getenv("GROQ_API_KEY")
groq_api = st.secrets["GROQ_API_KEY"]


# Initialize LLM
llm = ChatGroq(model="mistral-saba-24b", api_key=groq_api)

# Initialize session state for chat storage
if "chats" not in st.session_state:
    st.session_state.chats = {}  # Dictionary storing multiple chat histories
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None  # Tracks the selected chat title
if "new_chat_started" not in st.session_state:
    st.session_state.new_chat_started = False
if "user_query" not in st.session_state:
    st.session_state.user_query = ""  # Stores user input to clear later

# Function to get chat history (linked to session state)
def get_chat_history(session_id):
    if session_id not in st.session_state.chats:
        st.session_state.chats[session_id] = ChatMessageHistory()  # ✅ Use ChatMessageHistory
    return st.session_state.chats[session_id]

# Wrap LLM with session-based history
with_chat_history = RunnableWithMessageHistory(llm, get_chat_history)

# Streamlit App Title
st.header("🤖Q&A Chatbot with Conversational History")

# Sidebar: Start Fresh Chat Button
if st.sidebar.button("🆕 Start Fresh Chat"):
    st.session_state.new_chat_started = True
    st.session_state.current_chat = None
    st.rerun()

# If a fresh chat is started, get a new title
if st.session_state.new_chat_started:
    chat_title = st.sidebar.text_input("Enter chat title:", key="new_chat_title")

    if chat_title and chat_title not in st.session_state.chats:
        st.session_state.chats[chat_title] = ChatMessageHistory()  # ✅ Initialize ChatMessageHistory
        st.session_state.current_chat = chat_title
        st.session_state.new_chat_started = False
        st.rerun()

# Display Previous Chats in Sidebar
st.sidebar.subheader("📁 Previous Chats")
for title in st.session_state.chats.keys():
    if st.sidebar.button(title, key=f"chat_{title}"):
        st.session_state.current_chat = title
        st.session_state.new_chat_started = False
        st.rerun()

# Ensure a chat is selected before proceeding
if not st.session_state.current_chat:
    st.warning("Please start a fresh chat and enter a title to proceed.")
else:
    # Retrieve chat history for the selected session title (acting as session_id)
    session_id = st.session_state.current_chat
    chat_history = get_chat_history(session_id)

    # User Input Field
    user_input = st.text_input("Present your prompt here👇", value=st.session_state.user_query, key="user_input")

    if user_input:
        config = {"configurable": {"session_id": session_id}}
        response = with_chat_history.invoke(HumanMessage(content=user_input), config=config)
        response_text = response.content  # Extract response text

        # # ✅ Append user input and AI response correctly
        # chat_history.add_user_message(user_input)
        # chat_history.add_ai_message(response_text)

    # ✅ Ensure Human message appears first, then AI response, in latest-first order
    messages = list(chat_history.messages)
    for i in range(len(messages) - 1, -1, -2):  # Step -2 to pair human & AI messages
        if i >= 1 and isinstance(messages[i - 1], HumanMessage) and isinstance(messages[i], AIMessage):
            with st.chat_message("user"):
                st.write(messages[i - 1].content)  # Human input first
            with st.chat_message("assistant"):
                st.write(messages[i].content)  # AI response next
        elif isinstance(messages[i], HumanMessage):  # Handle unpaired HumanMessage
            with st.chat_message("user"):
                st.write(messages[i].content)
        elif isinstance(messages[i], AIMessage):  # Handle unpaired AIMessage
            with st.chat_message("assistant"):
                st.write(messages[i].content)



# Custom Sidebar Button Styling
sidebar_css = """
    <style>
        [data-testid="stSidebar"] button {
            width: 100%;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            background-color: white;
            transition: 0.2s ease-in-out;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #f0f2f6;
        }
    </style>
"""
st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)
