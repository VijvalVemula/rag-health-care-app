def extract_text_from_pdf(pdf_file):
    from PyPDF2 import PdfReader
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text