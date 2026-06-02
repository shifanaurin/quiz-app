import streamlit as st
from groq import Groq
import json

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_questions(topic, num_questions):
    prompt = f"""Generate {num_questions} multiple choice questions about {topic}.
    Return ONLY a JSON array with this exact format, no other text, no markdown:
    [
        {{
            "question": "question text here",
            "options": ["option1", "option2", "option3", "option4"],
            "answer": "correct option here"
        }}    ]"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    
    response_text = response.choices[0].message.content.strip()
    
    # Clean response (remove markdown if any)
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
        response_text = response_text.strip()
    
    questions = json.loads(response_text)
    return questions

# Page config
st.set_page_config(page_title="AI Quiz App", page_icon="🧠")
st.title("🧠 AI Powered Quiz App")
st.subheader("Enter any topic and I'll generate questions for you!")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False

# Start screen
if not st.session_state.quiz_started:
    topic = st.text_input("Enter a topic:", placeholder="e.g. Space, History, Python, Cricket...")
    num_questions = st.slider("Number of questions:", 3, 10, 5)
    
    if st.button("Generate Quiz 🚀"):
        if topic.strip():
            with st.spinner(f"Generating {num_questions} questions about {topic}..."):
                try:
                    st.session_state.questions = generate_questions(topic, num_questions)
                    st.session_state.quiz_started = True
                    st.session_state.topic = topic
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating questions: {e}")
        else:
            st.error("Please enter a topic!")

# Quiz screen
elif st.session_state.quiz_started and not st.session_state.quiz_complete:
    questions = st.session_state.questions
    q_index = st.session_state.current_question
    q = questions[q_index]
    
    st.markdown(f"**Topic: {st.session_state.topic}**")
    st.progress((q_index) / len(questions))
    st.markdown(f"### Question {q_index + 1} of {len(questions)}")
    st.markdown(f"**{q['question']}**")
    
    selected = st.radio("Choose your answer:", q["options"], key=f"q{q_index}")
    
    if not st.session_state.answered:
        if st.button("Submit Answer"):
            st.session_state.answered = True
            if selected == q["answer"]:
                st.session_state.score += 1
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")
    
    if st.session_state.answered:
        if q_index + 1 < len(questions):
            if st.button("Next Question ➡️"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            if st.button("See Results 🏆"):
                st.session_state.quiz_complete = True
                st.rerun()

# Results screen
else:
    score = st.session_state.score
    total = len(st.session_state.questions)
    percentage = (score / total) * 100
    
    st.title("🏆 Quiz Complete!")
    st.markdown(f"## Score: {score}/{total}")
    st.progress(percentage / 100)
    
    if percentage == 100:
        st.balloons()
        st.success("🌟 Perfect Score!")
    elif percentage >= 70:
        st.success("🎉 Great job!")
    elif percentage >= 50:
        st.warning("👍 Not bad!")
    else:
        st.error("📚 Keep practicing!")
    
    if st.button("🔄 Try Another Topic"):
        st.session_state.questions = []
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.quiz_started = False
        st.session_state.quiz_complete = False
        st.rerun()