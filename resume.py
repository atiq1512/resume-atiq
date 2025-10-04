import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Resume — Atiq Nurnatasha", layout="wide")

# --- HEADER ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("atiq.jpg", width=180, caption="Atiq Nurnatasha")

with col2:
    st.title("Atiq Nurnatasha binti Zainal Abidin")
    st.markdown("💻 **Information Technology Student | Aspiring Developer | Tech Enthusiast**")
    st.markdown(
        """
        📍 Batu Kurau, Perak  
        📧 [atiqnurnatasha15@gmail.com](mailto:atiqnurnatasha15@gmail.com)  
        📱 +60 11-5157 6711  
        🔗 [linkedin.com/in/atiqsha](https://linkedin.com/in/atiqsha)
        """
    )

st.markdown("---")

# --- MAIN LAYOUT ---
left, right = st.columns([1, 2])

# LEFT COLUMN
with left:
    st.subheader("🎓 Education")
    st.write("**Sekolah Kebangsaan Batu Kurau**, Perak (2008–2013)")
    st.write("**SMK Dato' Kamaruddin**, Batu Kurau, Perak (2014–2018)")
    st.write(
        "**Diploma in Information Technology (Digital Technology)** — Politeknik Sultan Abdul Halim Mu'adzam Shah, Kedah (2019–2022)"
    )
    st.write(
        "**Bachelor’s Degree in Information Technology** — Universiti Malaysia Kelantan (2023–2026)"
    )

    st.subheader("🛠 Skills")
    st.write(
        """
        - Programming: HTML, C++, Java  
        - Software: Microsoft Word, PowerPoint  
        - Languages: Malay (Native), English (Bilingual)  
        - Strengths: Problem Solving, Teamwork, Communication  
        """
    )

    st.subheader("🏆 Awards & Achievements")
    st.write("- Certificate of Industry Trainee in Information Technology (July 2022)")
    st.write("- Anugerah Kecemerlangan Akademik (June 2022)")
    st.write("- Certificate of Majlis Pra-Graduan (Souvenir Committee) (Jan 2022)")
    st.write("- 🥇 **Anugerah Pingat Ketua Jabatan (Oct 2023)**")

# RIGHT COLUMN
with right:
    st.subheader("💼 Work Experience")

    st.markdown("**Tadika APC**, Taiping, Perak — Babysitter & Kindergarten Teacher *(Jan 2019 – Mar 2019)*")
    st.write(
        """
        • Entertained children through games and creative activities.  
        • Prepared snacks and meals for children.  
        • Created lesson plans and teaching materials.  
        • Taught basic academic skills such as alphabets, colours, shapes, and number recognition.
        """
    )

    st.markdown("**Majlis Perbandaran Taiping (MPT)**, Taiping, Perak — IT Trainee *(Apr 2022 – Jul 2022)*")
    st.write(
        """
        • Provided technical support for system and network issues.  
        • Assisted team members and managers in resolving IT problems.  
        • Helped troubleshoot connectivity and data access errors.  
        """
    )

    st.subheader("📂 Projects")
    st.write(
        """
        - **Smart Water Sprinkler System** — IoT-based prototype with moisture sensors for efficient water use.  
        - **Portfolio Website** — Personal site built using HTML, CSS, and JavaScript to display achievements.  
        """
    )

st.markdown("---")
st.markdown("✅ *Last updated: October 2025*")
