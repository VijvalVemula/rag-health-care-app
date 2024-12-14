import streamlit as st
from agents.agent1 import extract_text_from_pdf
from agents.agent2 import query_pdf_data
from agents.agent3 import generate_answer_with_openai

# Apply custom CSS
with open("css/styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Title
st.title("Patient Health Record Query System")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload Patient Health Record (PDF)", type=["pdf"])

# Query Input
query = st.text_input("Ask a Question About the Patient's Health")

# Display PDF Text (if extracted)
if uploaded_pdf is not None:
    text = extract_text_from_pdf(uploaded_pdf)
    st.write("Extracted Text from PDF:")
    st.text_area("Patient's Health Record", text, height=300)

# Display the Answer
if query and uploaded_pdf is not None:
    with st.spinner("Processing your query..."):
        # Hierarchical Process with Agents
        extracted_data = query_pdf_data(text)
        answer = generate_answer_with_openai(query, extracted_data)
        st.subheader("Answer:")
        st.write(answer)