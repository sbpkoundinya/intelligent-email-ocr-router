from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

# Sample request model
class EmailRequest(BaseModel):
    email_body: str
    has_attachment: bool

# Placeholder for AI model logic
def classify_email(email_body: str, has_attachment: bool) -> Dict:
    # Mock classification logic
    if "loan" in email_body.lower():
        request_type = "Loan Inquiry"
        sub_request_type = "Application Status" if "application" in email_body.lower() else "General Inquiry"
    elif "transaction" in email_body.lower():
        request_type = "Fraud Alert"
        sub_request_type = "Unauthorized Transaction"
    else:
        request_type = None
        sub_request_type = None

    priority_source = "Body" if not has_attachment else "Attachment"
    duplicate_detection = "Not Flagged"  # Placeholder logic

    # Mock next steps guidance
    guidance = []
    if request_type == "Loan Inquiry":
        guidance.append("Review loan application portal")
    elif request_type == "Fraud Alert":
        guidance.append("Verify transaction history and contact support")

    return {
        "Predicted Request Types": [request_type] if request_type else [],
        "Predicted Sub-Request Types": [sub_request_type] if sub_request_type else [],
        "Priority Source": priority_source,
        "Duplicate Detection": duplicate_detection,
        "Next Steps Guidance": guidance or ["No specific guidance available."]
    }

@app.post("/classify")
def classify(email_request: EmailRequest):
    if not email_request.email_body.strip():
        return {
            "Predicted Request Types": [],
            "Predicted Sub-Request Types": [],
            "Priority Source": "None",
            "Duplicate Detection": "Not Applicable",
            "Next Steps Guidance": ["No specific guidance available."]
        }
    
    result = classify_email(email_request.email_body, email_request.has_attachment)
    return result
