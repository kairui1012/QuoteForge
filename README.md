# QuoteForge

QuoteForge is a mixed Java and Python project for turning natural-language input into structured quotation data. The repository currently contains the Python-based AI service, built with FastAPI. The Java application layer will be added alongside it as the project grows.

## Current Features

- FastAPI-based AI service
- Request validation with Pydantic
- Message parsing API scaffold
- Interactive OpenAPI documentation
- Docker support with Python 3.13

## Project Structure

```text
QuoteForge/
├── quoteflow-ai/
│   ├── ai-service/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   └── requirements.txt
│   ├── .dockerignore
│   └── Dockerfile
├── .gitignore
└── README.md
```

## Prerequisites

Choose one of the following:

- Python 3.13 and `pip`
- Docker Desktop or Docker Engine

## Run Locally

From the repository root:

```bash
cd quoteflow-ai/ai-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The service will be available at `http://localhost:8000`.

## Run with Docker

Build the image from the repository root:

```bash
docker build -t quoteforge-ai ./quoteflow-ai
```

Start the container:

```bash
docker run --rm -p 8000:8000 quoteforge-ai
```

## API Endpoints

### Parse a message

```http
POST /api/parse
Content-Type: application/json
```

Example request:

```bash
curl -X POST http://localhost:8000/api/parse \
  -H "Content-Type: application/json" \
  -d '{"message":"Create a quotation for 10 office chairs"}'
```

Current response:

```json
{
  "message": "Create a quotation for 10 office chairs",
  "length": 39
}
```

### Test endpoint

```bash
curl "http://localhost:8000/haha?message=hello"
```

## API Documentation

When the service is running, FastAPI provides interactive documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development Status

The current parsing endpoint validates input and returns the original message with its length. AI-powered extraction and the Java application layer are not implemented in this repository yet.
