import streamlit as st

# --- Page Settings ---
st.set_page_config(page_title="Resume — Atiq Nurnatasha", layout="wide")

# --- Header Section ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/180", width=180, caption="Atiq Nurnatasha")  # Replace with your profile photo

with col2:
    st.title("Atiq Nurnatasha")
    st.markdown("💻 **IT Student | Aspiring Developer | Tech Enthusiast**")
    st.write("📧 Email: atiqnurnatasha@gmail.com")
    st.write("📱 Phone: (+60) 115-1576711")
    st.write("🔗 LinkedIn: [linkedin.com/in/atiqsha](https://linkedin.com/in/atiqsha)")

st.markdown("---")

# --- Main Layout ---
left, right = st.columns([1, 2])

# Left column = Skills + Education
with left:
    st.header("🎓 Education")
    st.write("**Bachelor’s Degree in Information Technology**")
    st.write("University Malaysia Kelantan (2023–2026)")

    st.header("🛠 Skills")
    st.write("- Python & Streamlit")
    st.write("- Web Development")
    st.write("- Problem Solving")
    st.write("- Technical Support")
    st.write("- Communication & Teamwork")

# Right column = Work Experience + Projects
with right:
    st.header("💼 Work Experience")
    st.subheader("Intern — IT Department, Majlis Perbandaran Taiping (2022)")
    st.write("- Assisted staff with technical issues that occurred")
    st.write("- Provided support to team members and managers as needed")
    st.write("- Helped with various issues, including connection problems")

    st.header("📂 Projects")
    st.subheader("Smart Water Sprinkler System")
    st.write(
        "Developed an IoT-based smart sprinkler prototype with moisture sensors "
        "to optimize water usage and improve sustainability."
    )

    st.subheader("Portfolio Website")
    st.write(
        "Built a personal portfolio site using HTML, CSS, and JavaScript to showcase "
        "projects and achievements."
    )

st.markdown("---")
st.markdown("✅ *Last updated: October 2025*")
