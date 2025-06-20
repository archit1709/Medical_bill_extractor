import re

def clean_text(raw_text):
    # Remove unnecessary line breaks and extra spaces
    text = re.sub(r'\s+', ' ', raw_text)
    text = text.strip()
    return text
