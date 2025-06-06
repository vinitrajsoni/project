

import streamlit as st
from app.parser import extract_resume_data
from app.storage import save_result, load_all_results

st.set_page_config(page_title="Resume Skill Extractor", layout="centered")

st.title("📄 Resume Skill Extractor")

uploaded_file = st.file_uploader("Upload a PDF Resume", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting..."):
        extracted_data = extract_resume_data(uploaded_file)
        save_result(extracted_data)
    
    st.success("✅ Extraction complete!")
    st.subheader("Extracted Summary")
    st.json(extracted_data)

    st.subheader("✏️ Edit Extracted Data")

    name = st.text_input("Name", extracted_data.get("name", ""))
    email = st.text_input("Email", extracted_data.get("email", ""))
    skills = st.text_area("Skills (comma-separated)", ", ".join(extracted_data.get("skills", [])))
    experience = st.text_area("Experience", extracted_data.get("experience", ""))

    if st.button("💾 Save Edited Data"):
        edited_data = {
            "name": name,
            "email": email,
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "experience": experience
        }
        save_result(edited_data)
        st.success("Edited data saved!")

st.subheader("📁 Stored Results")

# Added search filter by name
search_name = st.text_input("🔎 Search by name")

all_data = load_all_results()

if search_name:
    filtered_data = [d for d in all_data if search_name.lower() in d.get("name", "").lower()]
else:
    filtered_data = all_data

for i, data in enumerate(filtered_data, 1):
    with st.expander(f"Result {i}"):
        st.json(data)
