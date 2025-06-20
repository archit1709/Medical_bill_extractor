import pytesseract
import cv2
from PIL import Image

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Improve accuracy
    text = pytesseract.image_to_string(gray)
    return text
