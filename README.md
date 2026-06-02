# 🧠 AI Powered Quiz App

An intelligent quiz generator that creates custom multiple-choice questions on **any topic** using Large Language Models (LLMs).

## 🚀 Live Demo

👉 **[Try the App Here](https://aigenerated-quiz-app.streamlit.app)** 

## ✨ Features

- 🎯 **Generate quizzes on ANY topic** — Space, History, Cricket, Python, anything!
- 🤖 **Powered by Groq LLM** (Llama 3.3 70B model) — super fast responses
- 🎨 **Clean, intuitive UI** built with Streamlit
- 📊 **Real-time scoring** with progress tracking
- 🎉 **Interactive feedback** — instant correct/wrong indication
- 🔄 **Replay option** — try unlimited topics

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web app framework |
| **Groq API** | LLM integration (Llama 3.3) |
| **JSON** | Data parsing |

## 📸 How It Works

1. Enter any topic you want to learn about
2. Choose number of questions (3-10)
3. AI generates custom multiple-choice questions
4. Answer questions and get instant feedback
5. See your final score with celebration animations 🎉

## 🏃‍♀️ Run Locally

### Prerequisites
- Python 3.8+
- Groq API Key (get free at [console.groq.com](https://console.groq.com))

### Installation

**Step 1: Clone this repository**

```bash
git clone https://github.com/shifanaurin/ai-quiz-app.git
cd ai-quiz-app
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Set up your API key**

Create a folder named `.streamlit` and inside it create a file `secrets.toml` with:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**Step 4: Run the app**

```bash
streamlit run quiz.py
```

**Step 5: Open in browser**

Visit `http://localhost:8501` 🎉

## 🌟 What I Learned

Building this project taught me:
- 🔌 How to integrate **LLM APIs** into applications
- 🔐 Managing **API keys securely** with environment secrets
- 📦 **Session state management** in Streamlit
- 🎨 Designing **multi-screen user flows**
- 🚀 **End-to-end deployment** on Streamlit Cloud

## 💡 Future Improvements

- [ ] Add difficulty levels (Easy/Medium/Hard)
- [ ] Support for image-based questions
- [ ] User authentication and leaderboard
- [ ] Multi-language support
- [ ] Export quiz results as PDF

## 👩‍💻 About the Developer

**Shifa Naurin**

CSE Student | AI & ML Intern @ IIT Palakkad | AI & DS Intern @ Techmindz | Published Malayalam Poet ✨

- 🌐 [LinkedIn](https://www.linkedin.com/in/shifa-naurin-a3584a367/)
- 💻 [GitHub](https://github.com/shifanaurin)
- 📍 Cannanore, Kerala, India

---

⭐ **If you found this project helpful, please give it a star!**

*Built with ❤️ and a lot of curiosity*
