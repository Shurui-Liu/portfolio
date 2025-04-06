# portfolio_app.py

import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="wide")

# ---- HEADER ----
st.title("👋 Hi, I'm Your Name Here")
st.subheader("Aspiring Software Engineer | Passionate about Full-Stack & AI")
st.write("Welcome to my interactive portfolio. Below are some of the projects I've worked on.")

# ---- PROJECTS ----
st.markdown("## 🚀 Projects")

project_data = [
    {
        "title": "Trip Planner App",
        "description": "Web-based travel planner using React, Flask, and Map APIs. Calculates optimized travel routes with user preferences.",
        "tech": "Python, Flask, React, OpenStreetMap",
        "link": "https://github.com/yourusername/trip-planner"
    },
    {
        "title": "Grocery Store Inventory System",
        "description": "Internal system for managing inventory and staff, using SpringBoot and MySQL with JSP frontend.",
        "tech": "Java, SpringBoot, MySQL, JSP",
        "link": "https://github.com/yourusername/grocery-inventory-system"
    },
    {
        "title": "Gradebook App",
        "description": "Python-based tool to manage and visualize grades, with CSV import/export and statistical insights.",
        "tech": "Python, Pandas, Streamlit",
        "link": "https://github.com/yourusername/gradebook-app"
    },
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
