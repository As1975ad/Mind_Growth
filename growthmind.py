import streamlit as st
import random

# 🏆 Motivational Quotes & Mood Messages
QUOTES = [
    "Failure is an opportunity to grow.",
    "I can learn to do anything I want.",
    "Challenges help me to grow.",
    "My effort and attitude determine my abilities.",
    "Feedback is constructive.",
    "I like to try new things.",
    "I am inspired by the success of others."
]

MOOD_MESSAGES = {
    "Happy": "That's great! Keep spreading positivity! 😊",
    "Sad": "Tough times don't last, but tough people do! 💪",
    "Motivated": "Keep going! Your dreams are worth it. 🚀",
    "Tired": "Take a break and come back stronger! 🔥"
}

#  Page Setup
st.set_page_config(page_title="AI Motivation Hub", layout="wide")

#  Custom CSS for Black Sidebar
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: black !important;
            color: white !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#  Sidebar with Image & Title
st.sidebar.title("🌱 Growth Mindset")
st.sidebar.image("image.png", use_container_width=True)
st.sidebar.write("### Stay Inspired & Keep Growing! 🚀")

#  Main Content
st.title("🎯 AI-Based Motivation Hub")
st.subheader("Get Your Daily Dose of Motivation")
st.success(f"🏆 **Today's Motivation:** {random.choice(QUOTES)}")

#  User Mood Input
mood = st.selectbox("How are you feeling today?", MOOD_MESSAGES.keys())
st.info(f"💡 **Motivation for You:** {MOOD_MESSAGES[mood]}")

st.markdown("---")
st.write("😊 *Stay positive and keep growing!*")



st.markdown("Created By Asad Jilani GIAIC (7534) Email : a.jee1975@gmail.com")