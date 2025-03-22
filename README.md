# Gen AI-Powered Email Classification & OCR Solution

## Overview
This project provides an AI-powered backend service to classify and extract data from emails, supporting:
- Request and sub-request type categorization
- Context-based data extraction
- Handling multi-request emails
- Priority-based extraction
- Duplicate detection
- Next-step guidance

## Features
- Uses **OpenAI, Tesseract, and FastAPI**
- Accepts emails and attachments
- Prioritizes email body or attachment based on context
- Provides confidence scores and recommended actions
- Deployable with **Docker** and integrates with **CI/CD**

## Sequence Diagram
![image](https://github.com/user-attachments/assets/ebd1f90b-5888-46e0-a662-b61cd99f6955)

## Installation
### Prerequisites
- Python 3.9+
- Docker (for containerization)
- GitHub Actions (for CI/CD)

### Setup
Clone the repository:
```bash
git clone https://github.com/sbpkoundinya/intelligent-email-ocr-router.git
cd intelligent-email-ocr-router
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the FastAPI server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Run in Docker
```bash
docker build -t intelligent-email-ocr-router .
docker run -p 8000:8000 intelligent-email-ocr-router
```

## API Endpoints
### Classify Email
```http
POST /classify
```
**Request Body:**
```json
{
  "email_body": "I need information about my loan application.",
  "has_attachment": true
}
```
**Response:**
```json
{
  "Predicted Request Types": ["Loan Inquiry"],
  "Predicted Sub-Request Types": ["Application Status"],
  "Priority Source": "Body",
  "Duplicate Detection": "Not Flagged",
  "Next Steps Guidance": ["Review loan application portal"]
}
```

## Running Tests
```bash
pytest
```

## CI/CD
This project uses **GitHub Actions** for:
- Running tests on push and PRs
- Building and pushing Docker images on the `main` branch

## Contributors
- [Your Name](https://github.com/your-profile)

## License
MIT License
