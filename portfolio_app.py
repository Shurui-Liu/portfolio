# portfolio_app.py

import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="wide")

# ---- HEADER ----
st.title("👋 Hi, I'm Shurui")
st.subheader("Software Engineer | Passionate about Full-Stack & AI")
st.write("Welcome to my interactive portfolio. Below are some of the projects I've worked on.")

# ---- PROJECTS ----
st.markdown("## 🚀 Projects")

project_data = [
    {
        "title": "AI Mood Companion App",
        "description": "an AI-empowered, multi-user SaaS web application tool for mental well-being. I developed the project's part that integrates LLM to offer real-time chats. Through prompt-engineering, I ensured this app help people identify their distorted thinking patterns and turn them into positive ones.",
        "tech": "React, MongoDB, OpenAI API",
        "live website": "https://moodcompanion.onrender.com/chat"
    },
    {
        "title": "NYC Trip Planner",
        "description": "A full-stack web application that helps users plan custom NYC trips by selecting starting points, destinations, and time constraints. The app uses optimization algorithms to generate the shortest multi-day itinerary that minimizes commuting time and maximizes visit coverage.",
        "tech": "JavaScript, Express, Python, Google Maps API",
        "link": "https://github.com/Shurui-Liu/NYC-Trip-Planner-Web"
    },
    {
        "title": "Grocery Store Inventory System",
        "description": "Internal system for managing inventory and staff, using SpringBoot and MySQL with JSP frontend.",
        "tech": "Java, SpringBoot, MySQL, JSP",
        "link": "https://github.com/yourusername/grocery-inventory-system"
    }
]

for project in project_data:
    st.markdown(f"### [{project['title']}]({project['link']})")
    st.write(project["description"])
    st.markdown(f"**Tech stack**: {project['tech']}")
    st.markdown("---")

# ---- SKILLS ----
st.markdown("## 🧠 Skills")
skills = [
    "Python", "Java", "JavaScript", "HTML/CSS", "React.js", 
    "Streamlit", "MySQL", "SpringBoot", "Flask", "Git/GitHub"
]
st.write(", ".join(skills))

# ---- CONTACT ----
st.markdown("## 📫 Contact")
st.write("📧 Email: your.email@example.com")
st.write("[🔗 LinkedIn](https://linkedin.com/in/yourprofile)")
st.write("[💻 GitHub](https://github.com/yourusername)")
