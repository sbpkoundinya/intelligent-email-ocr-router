import email
from email import policy
from email.parser import BytesParser
import pytesseract
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic model for email content input
class EmailRequest(BaseModel):
    email_body: str
    has_attachment: bool

# Function to parse .eml files and extract content
def parse_eml(file_path: str):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    
    body = msg.get_body(preferencelist=('plain', 'html')).get_content()
    
    attachments = []
    for part in msg.iter_attachments():
        filename = part.get_filename()
        content_type = part.get_content_type()
        content = part.get_payload(decode=True)
        attachments.append({
            'filename': filename,
            'content_type': content_type,
            'content': content
        })
    
    return body, attachments

# Function to perform OCR on image attachments (if any)
def perform_ocr_on_images(attachments):
    ocr_results = []
    for attachment in attachments:
        if attachment['content_type'].startswith('image'):
            image_data = io.BytesIO(attachment['content'])
            image = Image.open(image_data)
            text = pytesseract.image_to_string(image)
            ocr_results.append({
                'filename': attachment['filename'],
                'ocr_text': text
            })
    return ocr_results

# Placeholder function for email classification logic
def classify_email(email_content):
    # Placeholder classification logic based on email body
    body = email_content['body']
    has_attachment = len(email_content['attachments']) > 0
    
    request_type = "General Inquiry" if "query" in body.lower() else "Other"
    sub_request_type = "Account" if "account" in body.lower() else "Service"
    priority_source = "Attachment" if has_attachment else "Email"
    duplicate_detection = "Not Flagged"  # This would be implemented in your system

    return {
        "request_type": request_type,
        "sub_request_type": sub_request_type,
        "priority_source": priority_source,
        "duplicate_detection": duplicate_detection
    }

# Endpoint to handle email content via JSON input
@app.post("/process_email")
async def process_email(request: EmailRequest):
    # Process the email with the provided body and attachment flag
    email_content = {
        "body": request.email_body,
        "attachments": [] if not request.has_attachment else ["Attachment placeholder"]
    }

    # Classify the email
    classification_result = classify_email(email_content)

    return {"classification_result": classification_result, "message": "Email processed successfully"}

# Endpoint to upload and process .eml file
@app.post("/upload_eml")
async def upload_eml(file: UploadFile = File(...)):
    # Save the uploaded .eml file temporarily
    file_path = "temp_email.eml"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Parse the .eml file to extract content
    body, attachments = parse_eml(file_path)

    # Perform OCR on image attachments
    ocr_results = perform_ocr_on_images(attachments)

    # Combine email content and OCR results
    email_content = {
        "body": body,
        "attachments": ocr_results
    }

    # Classify the email
    classification_result = classify_email(email_content)

    return {
        "classification_result": classification_result,
        "email_body": body,
        "ocr_results": ocr_results,
        "message": "EML file processed successfully"
    }
