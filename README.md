# Fraud Detection Model Microservice

A FastAPI-based microservice for fraud detection using a pre-trained machine learning model. You can run it either via Docker or from the source code.

## Running the Service
### Option 1: Using Docker
1. **Pull the Docker Image**:
To pull the Docker image from GitHub Container Registry:
```bash
docker pull ghcr.io/png261/fraud-dection-model-microservice:latest
```
2. **Run the Docker Container**
```bash
docker run -d -p 8000:8000 ghcr.io/png261/fraud-dection-model-microservice:latest
```
### Option 2: Running from Source Code
1. **Clone the Repository**:
```bash
git clone https://github.com/png261/fraud-dection-model-microservice.git
cd fraud-dection-model-microservice
```
2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run the Microservice:**
```bash
uvicorn app.main:app --reload
```
The service will be available at [http://localhost:8000](http://localhost:8000)

