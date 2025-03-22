
# Email Classifier with OCR and Routing Backend (FastAPI)

This backend service classifies emails, extracts fields, detects duplicates, and routes requests based on content and context.

## Features
- Email classification into request/sub-request types
- OCR/priority-aware field extraction
- Duplicate detection
- Smart routing to appropriate teams
- Confidence score included in predictions

## Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Place trained model files (`email_classifier_with_priority_model.joblib`, `tfidf_vectorizer.joblib`) in root directory.
3. Run server: `uvicorn app.main:app --reload`
4. Visit Swagger docs at: `http://127.0.0.1:8000/docs`

## Endpoints
- `/classify-email`
- `/extract-fields`
- `/check-duplicate`
- `/route-request`
- `/health`
