# 🤖 Q&A Chatbot with Conversational History

An AI-powered chatbot built with **Streamlit** and **LangChain** that retains conversational history for multiple chat sessions. The chatbot leverages **Groq API** for responses and provides a seamless Q&A experience with stored chat sessions.

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](<screenshot_home.png>)

### 💬 Chat Interface
![Chat Interface](<screenshot_chat.png>)

### 📁 Chat History
![Chat History](<screenshot_chat_history.png>)

### 🎨 Sidebar & Theme
![Sidebar](<screenshot_sidebar.png>)

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
  git clone https://github.com/yourusername/streamlit-chatbot.git
  cd streamlit-chatbot
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

## 📌 Future Enhancements

- 🔹 **Improve AI Model**: Integrate GPT-4 or fine-tune responses.
- 🔹 **Dark Mode**: Add theme switch for better accessibility.
- 🔹 **Export Chat History**: Save conversations as a text or PDF file.
- 🔹 **Better Styling**: Enhance UI with more animations and layouts.

---

## 🤝 Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a Pull Request.

---

## 📝 License

This project is **open-source** and available under the MIT License.

---

## 📬 Contact

For any queries, feel free to reach out:

- 📧 Email: your.email@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)
- 💼 LinkedIn: [Your Profile](https://www.linkedin.com/in/yourprofile/)

Happy coding! 🚀

