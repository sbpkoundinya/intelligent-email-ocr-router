import pytest
from fastapi.testclient import TestClient
from main import app  # Ensure this matches the filename of your FastAPI app

client = TestClient(app)

def test_classify_email_without_attachment():
    email_data = {
        "email_body": "I need information about interest rates for home loans.",
        "has_attachment": False
    }
    response = client.post("/classify", json=email_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "Predicted Request Types" in response_json
    assert "Predicted Sub-Request Types" in response_json
    assert "Priority Source" in response_json
    assert "Duplicate Detection" in response_json
    assert "Next Steps Guidance" in response_json

def test_classify_email_with_attachment():
    email_data = {
        "email_body": "Please find the attached document regarding my loan application.",
        "has_attachment": True
    }
    response = client.post("/classify", json=email_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["Priority Source"] in ["Body", "Attachment"]
    assert "Predicted Request Types" in response_json

def test_duplicate_email_detection():
    email_data = {
        "email_body": "I am reporting an unauthorized transaction on my credit card.",
        "has_attachment": False
    }
    response = client.post("/classify", json=email_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["Duplicate Detection"] in ["Flagged", "Not Flagged"]

def test_guidance_provided():
    email_data = {
        "email_body": "I need help updating my account details.",
        "has_attachment": False
    }
    response = client.post("/classify", json=email_data)
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json["Next Steps Guidance"]) > 0
    assert response_json["Next Steps Guidance"][0] != "No specific guidance available."
