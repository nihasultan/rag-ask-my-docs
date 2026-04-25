import streamlit as st
from ingestion import process_uploaded_file
from pipeline import initialize, ask

st.set_page_config(page_title="Ask My Docs", layout="wide")

st.title("📄 Ask My Docs")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    initialize(uploaded_file)

    query = st.text_input("Ask a question about your document:")

    if query:
        with st.spinner("Thinking..."):
            answer, sources = ask(query)

        st.subheader("Answer")
        st.markdown(answer)

        st.subheader("Sources")
        for s in sources:
            st.write(f"{s['source']} - Page {s['page']}")