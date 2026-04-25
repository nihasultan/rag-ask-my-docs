from pypdf import PdfReader

def load_and_process_pdfs(file_path, file_name):
    reader = PdfReader(file_path)
    chunks = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            text = text.replace("\n", " ").strip()

            chunks.append({
                "text": text,
                "source": file_name,   
                "page": i + 1
            })

    return chunks


def process_uploaded_file(uploaded_file):
    file_path = "uploaded.pdf"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    return file_path, uploaded_file.name