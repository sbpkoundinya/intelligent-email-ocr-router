# Gen AI-Powered Email Processing System

## 1. Overview
This project is a Gen AI-powered email classification and OCR solution that:
- Extracts, interprets, and categorizes emails into request & sub-request types
- Performs context-based data extraction
- Handles multi-request emails with primary intent detection
- Prioritizes email content over attachments
- Detects duplicate emails & routes requests appropriately
- Supports real-time & batch processing
- Logs structured data into ELK for auditing & monitoring

## 2. Tech Stack
- **AI Models**: OpenAI, Hugging Face NLP
- **Framework**: Python (Flask/FastAPI)
- **Storage & Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Containerization**: Docker, Kubernetes
- **CI/CD**: GitHub Actions

## 3. Sequence Diagram
<img width="354" alt="image" src="https://github.com/user-attachments/assets/56097002-b39e-4b71-8d9b-0eabadd6cbbf" />

## 4. Request & Sub-Request Types Considered
The system classifies emails into the following **request types** and their respective **sub-request types**:

### Money Movement
- Fund Transfer
- Wire Transfer
- ACH Payment
- Check Processing
- FX Conversion
- Loan Disbursement
- Recurring Payment Setup

### Account Management
- New Account Opening
- Account Closure
- Account Upgrade/Downgrade
- Beneficiary Update
- Joint Account Addition

### Adjustments & Reconciliation
- Fee Waiver Request
- Disputed Transaction
- Interest Rate Adjustment
- Balance Correction
- Reversal Request

### Closing & Notice
- Account Closing Request
- Loan Payoff & Closure
- Termination of Credit Line
- Maturity Notice

### Credit & Loans
- Credit Limit Increase/Decrease
- Loan Application
- Mortgage Refinance
- Payment Holiday Request

### Investment & Treasury
- Securities Trade Request
- Asset Reallocation
- Dividend Reinvestment
- Portfolio Rebalancing

### Compliance & Security
- KYC/AML Documentation Update
- Fraud Alert & Investigation
- Data Privacy Request

### General Support
- Account Access Issues
- Password Reset Request
- Transaction Status Inquiry
- Statement Request
- System Downtime Report
- Customer Complaint & Feedback
- Request for Product Information
- Help with Mobile App or Online Banking
- Contact Information Update

## 5. Setup & Installation
### Prerequisites
- Python 3.8+
- Docker & Docker Compose
- ELK Stack (for logging & monitoring)

### Installation
```bash
# Clone repository
git clone <repo_url>
cd project_root

# Install dependencies
pip install -r requirements.txt

# Run the API service
python src/api/app.py
```

### Running with Docker
```bash
# Build and run containers
docker-compose up --build
```

## 6. API Usage
The service exposes an API endpoint to process emails.
### Endpoint: `POST /process-email`
- Accepts `.eml` file as input
- Returns structured JSON output with request classification, extracted fields, confidence score, and duplicate detection status

## 7. CI/CD Pipeline
The project includes a CI/CD pipeline using **GitHub Actions** to automate:
- Running unit tests
- Building Docker images
- Deploying to a cloud/on-prem environment

### Running Tests Locally
```bash
pytest tests/
```

## 8. Logging & Monitoring
- All processed emails are logged into **Elasticsearch** for audit & debugging
- **Kibana** dashboards provide analytics & insights

## 9. Sample Test Cases
Automated test cases cover different **request-sub-request** classifications. The test suite is included in the `tests/` directory.
```bash
pytest tests/test_classification.py
```

## 10. Sample `.eml` Files
The package includes sample `.eml` files for all request & sub-request types, located in the `sample_emails/` directory.
- Each file corresponds to a specific **request & sub-request type**
- Some files include **attachments** when necessary (e.g., Closing & Notice cases)
- The test suite automatically verifies classification accuracy using these samples


## 11. Future Enhancements
- Support for multilingual email processing
- Integration with additional financial systems
- Improved NLP models for better classification accuracy

---

This document provides a comprehensive overview of the solution. Feel free to modify based on your specific deployment needs! 🚀
