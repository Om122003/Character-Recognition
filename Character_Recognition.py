# Import the required libraries
from PIL import Image
import pytesseract



def ocr_image_to_text(image_path):
    """
    Extract text from the given image using pytesseract OCR.
    
    :param image_path: Path to the input image
    :return: Extracted text as a string
    """
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Convert image to string using pytesseract
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
image_path = 'sample_image.png'  # Replace with your image path
text = ocr_image_to_text(image_path)

if text:
    print("Extracted Text:\n")
    print(text)
else:
    print("No text extracted or error occurred.")
# Import the required libraries
from PIL import Image
import pytesseract



def ocr_image_to_text(image_path):
    """
    Extract text from the given image using pytesseract OCR.
    
    :param image_path: Path to the input image
    :return: Extracted text as a string
    """
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Convert image to string using pytesseract
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
image_path = 'sample_image.png'  # Replace with your image path
text = ocr_image_to_text(image_path)

if text:
    print("Extracted Text:\n")
    print(text)
else:
    print("No text extracted or error occurred.")
# Import the required libraries
from PIL import Image
import pytesseract


def ocr_image_to_text(image_path):
    """
    Extract text from the given image using pytesseract OCR.
    
    :param image_path: Path to the input image
    :return: Extracted text as a string
    """
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Convert image to string using pytesseract
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
image_path = 'sample_image.png'  # Replace with your image path
text = ocr_image_to_text(image_path)

if text:
    print("Extracted Text:\n")
    print(text)
else:
    print("No text extracted or error occurred.")
# Import the required libraries
from PIL import Image
import pytesseract



def ocr_image_to_text(image_path):
    """
    Extract text from the given image using pytesseract OCR.
    
    :param image_path: Path to the input image
    :return: Extracted text as a string
    """
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Convert image to string using pytesseract
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
image_path = 'sample_image.png'  # Replace with your image path
text = ocr_image_to_text(image_path)

if text:
    print("Extracted Text:\n")
    print(text)
else:
    print("No text extracted or error occurred.")
