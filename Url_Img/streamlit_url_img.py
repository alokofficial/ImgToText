import streamlit as st
import requests
import json

def ocr_space_url(url, overlay=False, api_key='K83551900988957', language='eng'):
    payload = {
        'url': url,
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language
    }
    r = requests.post('https://api.ocr.space/parse/image', data=payload)
    result = r.content.decode()
    return json.loads(result)

def extract_text(parsed_result):
    if 'ParsedResults' in parsed_result and len(parsed_result['ParsedResults']) > 0:
        parsed_text = parsed_result["ParsedResults"][0]["ParsedText"]
        lines = parsed_text.split('\r\n')
        extracted_text = "\r\n".join(lines[:4]) + '\r\n '
        return extracted_text
    else:
        return "No text found in OCR result"

# Streamlit application
st.title("OCR Space URL Text Extractor")

# Input URL
image_url = st.text_input("Enter the URL of the image:", "")

if image_url:
    # Display the input image
    st.image(image_url, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Extracting text...")

    # Perform OCR on the provided URL
    ocr_result = ocr_space_url(url=image_url, language='eng')

    # Extract text from the OCR result
    extracted_text = extract_text(ocr_result)

    # Display the extracted text
    st.write("Extracted Text:")
    st.text(extracted_text)


