import os
import pandas as pd
from ocr import extract_text_from_image
from clean_text import clean_text
from extract_info import extract_info

def process_image(image_path):
    raw_text = extract_text_from_image(image_path)
    cleaned = clean_text(raw_text)
    data = extract_info(cleaned)

    # Convert to DataFrame for CSV/Excel output
    df = pd.DataFrame([data])

    # Save to CSV
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    csv_path = os.path.join("output", f"{base_name}.csv")
    excel_path = os.path.join("output", f"{base_name}.xlsx")

    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)

    print(f"Saved results:\nCSV → {csv_path}\nExcel → {excel_path}")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    process_image("input/bill1.png")
