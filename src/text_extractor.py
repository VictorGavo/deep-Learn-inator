# text_extractor.py: Extracts and processes text from newsletters, online books, and other text sources.
# - Handle extraction of text from online newsletters, eBooks (PDF, ePub)
# - Use appropriate APIs or libraries depending on the source format
# - Return extracted text

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_text_from_epub(file_path):
    # Open the ePub file and extract text
    book = epub.read_epub(file_path)
    text_content = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            text_content.append(soup.get_text())
    return '\n'.join(text_content)

def extract_text(file_path, file_type='epub'):
    # Determine the file type and call the corresponding function
    if file_type == 'epub':
        return extract_text_from_epub(file_path)
    else:
        raise ValueError("Unsupported file type. Currently supports 'epub' only.")

# Future enhancements can include additional formats such as PDF or other e-book formats.
# TODO| PyPDF2 For DMing needs
