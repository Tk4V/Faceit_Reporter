from PIL import Image
import pytesseract
import requests
from io import BytesIO
import dropbox
import os
import shutil



with open("token.txt", "r") as f:
    token = f.read()

dbx = dropbox.Dropbox(token)

def perform_ocr(image):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

def save_to_file(text, output_file="output.txt"):
    # Save the text to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # Replace 'your_image_url' with the actual URL of your image file
    image_url = 'https://uc071072b6894c12c1cc2cf4322e.previews.dropboxusercontent.com/p/thumb/ACJzpYtydaZI4JIn-CEJYnfB_J85AGuIl9pD5oLZCeXaw2Z2-pYrKHR03xISvm_TnGDk5BE81YPvz-kqymwSEpN0MjBnSZfj8XUcU2WdajlEhAspzBNWhlnXCfY0tVNb5QTWbwFJ0cvMu4V49zWA-iNkj9uoj7tV6R9KbfNLesfxkHDxqSQXP02n5x0ii93bvevYYMbBpxhuSHpy4sPFP5YxAgqWhDG8glER2LHqYhSRh_HE0eXzBOi0v200olV8BJQIcXumyFT3FahyG3gncANRABaKhW9dwOAY9C1MC4AeF0V65gX3u5aEK62wneLBnoMmx09NfyqmxCm81m3Od9fRBAND-igl151l2JOOi4t44FGpFw80aOX2JkzXUgYMpjPqnY-FgddEMnnE6KPNaFbC/p.jpeg'
    # Download the image using requests and BytesIO
    response = requests.get(image_url)
    response.raise_for_status()

    # Print or check the content before attempting to open it as an image
    print(response.content)

    # Open the image from BytesIO
    try:
        img = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    # Perform OCR on the downloaded image
    result_text = perform_ocr(img)

    # Save the recognized text to a file
    save_to_file(result_text, output_file="output.txt")

    # Print a confirmation message
    print(f"Recognized text saved to 'output.txt'")

