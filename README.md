# Chatbot with conversational history using LangChain & Groq  

Welcome to **LangChain Groq Chat** – a chatbot that actually remembers what you say!  

This project lets you chat with an AI that **remembers your past messages within the same session**. It's like having multiple conversations at once, each with its own memory. Built with **LangChain, Groq API, and Python**, this chatbot is great for building AI assistants that can recall context.  

---

## What’s Cool About This?  

- **Memory for Each Session** – Your chat history is stored separately for each session.  
- **Forgetful but Smart** – It only remembers things **inside the same session** (like talking to different people).  
- **Uses Groq’s Powerful AI** – Chatbot responses are generated using the **mistral-saba-24b** model.  
- **Lightweight & Easy to Use** – No complex setup required. Just run and start chatting.  

---

## How It Works (In Simple Words)  

Imagine you have two separate chats:  

**Chat 1:**  
- You: "Hey! I’m Beast, an AI Engineer at Microsoft."  
- AI: "Nice to meet you, Beast! What can I do for you?"  
- Later… You: "What’s my job?"  
- AI: "You’re an AI Engineer at Microsoft!" *(It remembers.)*  

**Chat 2 (New session):**  
- You: "Hey, I’m 22 years old now."  
- AI: "That’s great!"  
- Later… You: "What’s my job?"  
- AI: "I don’t know, you didn’t tell me yet." *(It doesn’t mix sessions.)*  

Each session is like a separate chatroom. It remembers things inside but doesn’t mix them up.  

---

## Getting Started (Setup in 2 Minutes)  

### 1. Clone the Project  
```sh
git clone https://github.com/MeeturiAjay/Chatbot_with_conversational_history
cd Chatbot_with_conversational_history
