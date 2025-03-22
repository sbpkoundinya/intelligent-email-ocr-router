# 📧 Intelligent Email Classifier Backend (FastAPI)

This backend solution intelligently classifies emails, performs OCR-based data extraction, detects duplicates, and routes service requests—optimized for financial institutions.

## 🔁 Sequence Diagram
```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant FastAPI Backend
    participant Model
    participant Routing Engine

    User->>Frontend: Submit Email (Subject, Body, Attachment Info)
    Frontend->>FastAPI Backend: API Call (/classify-email)
    FastAPI Backend->>Model: Prepare Features and Predict
    Model-->>FastAPI Backend: Sub-request Type & Confidence
    FastAPI Backend->>Routing Engine: Route Based on Prediction
    Routing Engine-->>FastAPI Backend: Target Team
    FastAPI Backend-->>Frontend: Return Prediction, Score, Routing Info
    Frontend-->>User: Display Results
```

## 🚀 Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `uvicorn app.main:app --reload`
3. Access docs: `http://localhost:8000/docs`

## ✅ Automated Testing Summary
- sample_test_inputs.json
- sample_test_scenarios.csv
- test_email_classifier.py
Run tests: `python test_email_classifier.py`
