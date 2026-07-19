import streamlit as st
from src.generator import generate_quiz

st.set_page_config(
    page_title="AI-Powered Sports Quiz",
    page_icon="🏆",
    layout="centered"
)

st.title("🏆 AI-Powered Sports Quiz Generation Agent")
st.write("Generate fresh sports quizzes using AI, web search, and retrieved knowledge.")

# Sidebar
st.sidebar.header("Quiz Settings")

sport = st.sidebar.selectbox(
    "Select a Sport",
    ["Cricket", "Football", "Tennis", "Badminton", "Basketball"]
)

difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Store quiz in session state
if "quiz" not in st.session_state:
    st.session_state.quiz = None

if st.sidebar.button("Generate Quiz"):
    with st.spinner("Generating your quiz..."):
        try:
            st.session_state.quiz = generate_quiz(sport, difficulty)
        except Exception as e:
            st.error(f"Error generating quiz: {e}")

# Display quiz
if st.session_state.quiz:
    st.subheader(f"Sport: {sport}")
    st.write(f"**Difficulty:** {difficulty}")

    st.markdown(st.session_state.quiz)

    if st.button("🔄 Regenerate Quiz"):
        with st.spinner("Generating a new quiz..."):
            try:
                st.session_state.quiz = generate_quiz(sport, difficulty)
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("👈 Select a sport and difficulty, then click Generate Quiz.")