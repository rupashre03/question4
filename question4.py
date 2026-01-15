import streamlit as st
import nltk
from PyPDF2 import PdfReader

# Ensure punkt tokenizer is available
nltk.download("punkt", quiet=True)

st.set_page_config(page_title="PDF Sentence Chunker (NLTK)", layout="wide")

st.title("PDF Sentence Chunker Demo")
st.write(
    "Upload a PDF file, extract text, and split it into sentences using "
    "NLTK sentence tokenizer."
)

# Step 1: Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        # Step 2: Extract text from PDF
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        st.subheader("Basic Information")
        st.write(f"Number of pages: **{len(reader.pages)}**")
        st.write(f"Total characters extracted: **{len(text)}**")

        if not text.strip():
            st.warning("No text could be extracted from this PDF.")
        else:
            # Step 3: Sentence tokenization
            sentences = nltk.sent_tokenize(text)
            st.success(f"Number of detected sentences: {len(sentences)}")

            # Step 4: Display sentences 58–68
            st.subheader("Sentence Chunks (Index 58 to 68)")

            start = 58
            end = 68

            for i in range(start, min(end, len(sentences))):
                st.markdown(f"**{i}**. {sentences[i]}")

    except Exception as e:
        st.error(f"Error reading PDF: {e}")
else:
    st.info("Please upload a PDF to begin.")
