import re


def extract_info(text):
    data = {}

    # Doctor Name
    match = re.search(r'(Dr\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b', text)
    data['Doctor Name'] = match.group(1) if match else 'Not Found'
    

    # Bill Number
    match = re.search(r'Bill\s*No\.?\s*[:\-]?\s*([A-Za-z0-9]+)', text, re.IGNORECASE)
    data['Bill Number'] = match.group(1) if match else 'Not Found'

    # Patient Name
    match = re.search(r'Patient\s*Name[:\-]?\s*([A-Z][a-z]+\s+[A-Z][a-z]+)', text, re.IGNORECASE)
    data['Patient Name'] = match.group(1) if match else 'Not Found'

    # Date
    match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', text)
    data['Date'] = match.group(1) if match else 'Not Found'

    # Amount
    match = re.search(r'Amount[:\-]?\s*₹?\s?(\d+\.\d{2})', text, re.IGNORECASE)
    data['Amount'] = match.group(1) if match else 'Not Found'

    return data
