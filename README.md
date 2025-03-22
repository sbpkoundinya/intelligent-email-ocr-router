# Gen AI-Powered Email Processing System  
## Overview  
- Extracts, interprets, and categorizes emails  
- Context-based data extraction & duplicate detection  
- Real-time & batch processing with ELK logging  

## Setup & Installation  
### Prerequisites  
- Python 3.8+, Docker, ELK Stack  

### Installation  
```bash  
pip install -r requirements.txt  
python src/api/app.py  
```  

### Running with Docker  
```bash  
docker-compose up --build  
```  

## Usage  
- API Endpoint: `POST /process-email`  
