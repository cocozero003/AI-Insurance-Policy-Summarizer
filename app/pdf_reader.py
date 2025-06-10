
from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(file_bytes):
    reader = PdfReader(io.BytesIO(file_bytes))
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
