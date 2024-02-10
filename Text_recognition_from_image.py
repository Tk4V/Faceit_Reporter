from PIL import Image
import pytesseract

def perform_ocr(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img)

    return text

def save_to_file(text, output_file="output.txt"):
    # Save the text to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the actual path to your image file
    image_path = 'photo_2024-02-10_15-20-34.jpg'

    # Perform OCR on the image
    result_text = perform_ocr(image_path)

    # Save the recognized text to a file
    save_to_file(result_text, output_file="output.txt")

    # Print a confirmation message
    print(f"Recognized text saved to 'output.txt'")
