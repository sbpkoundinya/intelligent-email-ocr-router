import email
from email import policy
from email.parser import BytesParser
import pytesseract
from PIL import Image
import io

def parse_eml(file_path):
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
