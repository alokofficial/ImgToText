import requests
import json
import os
from dotenv import load_dotenv
load_dotenv() 


# def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
#     payload = {
#         'isOverlayRequired': overlay,
#         'apikey': api_key,
#         'language': language
#     }
#     with open(filename, 'rb') as f:
#         r = requests.post('https://api.ocr.space/parse/image',
#                           files={filename: f},
#                           data=payload)
#     result = r.content.decode()
#     return json.loads(result)

def ocr_space_url(url, overlay=False, api_key= os.getenv("api_key"), language='eng'):
    payload = {
        'url': url,
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language
    }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload)
    result = r.content.decode()
    return json.loads(result)

def extract_text(parsed_result):
    # print("OCR API Response:")
    # print(json.dumps(parsed_result, indent=4))  # Pretty-print the response for debugging
    if 'ParsedResults' in parsed_result and len(parsed_result['ParsedResults']) > 0:
        parsed_text = parsed_result["ParsedResults"][0]["ParsedText"]
        lines = parsed_text.split('\r\n')
        extracted_text = "\r\n".join(lines[:4]) + '\r\n '
        return extracted_text
    else:
        return "No text found in OCR result"

# Use examples:
# test_file_result = ocr_space_file(filename='./example_image.png', language='pol')
test_url_result = ocr_space_url(url='https://i.redd.it/56cnisa9qyia1.jpg' , language='eng')

# Extract and print the specific text from the file result
# file_text = extract_text(test_file_result)
# print("Extracted text from file:")
# print(file_text)

# Extract and print the specific text from the URL result
url_text = extract_text(test_url_result)
print("Extracted text from URL:")
print(url_text)

