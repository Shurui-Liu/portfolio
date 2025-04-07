import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="Shurui's Portfolio", page_icon="💼", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
    body {
        background-color: #f5f0e1;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
profile_image = Image.open("./profile_photo.jpg")

col1, col2 = st.columns([3, 1])
with col1:
    st.title("👋 Hi, I'm Shurui")
    st.subheader("💻 Software Engineer | Passionate about Full-Stack & AI")
    st.write("Welcome to my interactive portfolio. Below are some of the projects I've worked on.")
with col2:
    st.image(profile_image, width=150)

st.markdown("---")

# ---- PROJECTS ----
st.markdown("## 🚀 Projects")

project_data = [
    {
        "title": "AI Mood Companion App",
        "description": (
            "An **AI-powered**, multi-user **SaaS** web application for mental well-being. "
            "I developed the LLM-integrated chat feature using prompt engineering to help users "
            "identify and reframe distorted thinking patterns."
        ),
        "tech": "React, MongoDB, OpenAI API",
        "link": "https://moodcompanion.onrender.com/chat"
    },
    {
        "title": "NYC Trip Planner",
        "description": (
            "A full-stack app that generates optimized, multi-day itineraries for NYC travelers "
            "based on their chosen locations and time constraints."
        ),
        "tech": "JavaScript, Express, Python, Google Maps API",
        "link": "https://github.com/Shurui-Liu/NYC-Trip-Planner-Web"
    },
    {
        "title": "Grocery Store Inventory System",
        "description": (
            "An internal system for managing inventory and staff. "
            "Built using Java, with SpringBoot backend and JSP frontend."
        ),
        "tech": "Java, SpringBoot, MySQL, JSP",
        "link": "https://github.com/yourusername/grocery-inventory-system"
    }
]

for project in project_data:
    with st.container():
        cols = st.columns([1, 4])
        with cols[0]:
            st.markdown("📌")
        with cols[1]:
            st.markdown(f"### [{project['title']}]({project['link']})")
            st.write(project["description"])
            st.markdown(f"**Tech stack**: {project['tech']}")
    st.markdown("---")
# ---- SKILLS ----
st.markdown("## 🧠 Skills")
skills = [
    "Python", "Java", "JavaScript", "HTML/CSS", "React.js", 
    "SaaS", "MySQL", "API", "Git/GitHub"
]
st.markdown("**Languages & Tools:**")
st.markdown("✅ " + " | ✅ ".join(skills))

st.markdown("---")

# ---- CONTACT ----
st.markdown("## 📫 Contact")

contact_cols = st.columns(3)
contact_cols[0].write("📧 **Email:**  shurui.liu.710@gmail.com")

contact_cols[1].markdown("[🔗 **LinkedIn**](https://www.linkedin.com/in/shurui-liu33/)")
contact_cols[2].markdown("[💻 **GitHub**](https://github.com/Shurui-Liu)")
