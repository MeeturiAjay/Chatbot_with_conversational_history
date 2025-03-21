# 🤖 Q&A Chatbot with Conversational History

An AI-powered chatbot built with **Streamlit** and **LangChain** that retains conversational history for multiple chat sessions. The chatbot leverages **Groq API** for responses and provides a seamless Q&A experience with stored chat sessions.

---

## Have the Demo!💻
[![Application Demo](meeturis-conversational-chatbot-with-history.streamlit.app/)](https://meeturis-conversational-chatbot-with-history.streamlit.app/)

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](https://raw.githubusercontent.com/MeeturiAjay/Chatbot_with_conversational_history/refs/heads/main/Screenshots/Screenshot%202025-03-21%20152836.png)

### 💬 Chat Interface
![Chat Interface](https://raw.githubusercontent.com/MeeturiAjay/Chatbot_with_conversational_history/refs/heads/main/Screenshots/Screenshot%202025-03-21%20153504.png)


---

## 🚀 Features

- ✅ **Conversational History**: Saves chat history for multiple sessions.
- ✅ **Multiple Chat Sessions**: Users can start fresh chats and access past conversations.
- ✅ **Clean & Interactive UI**: Built using Streamlit with a modern and user-friendly design.
- ✅ **Groq API Integration**: Uses `mistral-saba-24b` for accurate responses.
- ✅ **Dynamic Sidebar**: Displays chat titles and options for a new conversation.
- ✅ **Custom Styles**: Sidebar buttons are styled for better usability.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive UI development.
- **AI Model**: [Groq API](https://groq.com/) - Chat model (`mistral-saba-24b`).
- **Backend**: [LangChain](https://www.langchain.com/) - Handles AI interactions.
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/) - Loads API keys securely.

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
  git clone https://github.com/MeeturiAjay/Chatbot_with_conversational_history.git
  cd Chatbot_with_conversational_history
```

### 2️⃣ Install Dependencies
```bash
  pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add:
```env
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application
```bash
  streamlit run app.py
```

---

## 🎯 Usage Guide

1. Start the chatbot by running the Streamlit app.
2. Click on **Start Fresh Chat** in the sidebar to begin a new session.
3. Enter a chat title to save and organize conversations.
4. Type your queries in the text input box and get AI-generated responses.
5. Access previous chats from the sidebar anytime.

---

## 📬 Contact

For any queries, feel free to reach out:

- 📧 Email: meeturiajaykumar.23@gmail.com
- 💼 LinkedIn: [Profile](https://www.linkedin.com/in/meeturi-ajay-kumar-a02743248/)

Happy coding! 🚀

