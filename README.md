# OSM Image API 🗺️
> A FastAPI-powered REST API for analyzing street-level images — built as a learning exercise before contributing to Humanitarian OpenStreetMap (HOT).

---

## Description

OSM Image API accepts an uploaded street-level image and returns basic analysis metadata relevant to road condition tagging. It predicts time of day from brightness, assigns a mock surface type, and extracts image dimensions and format — simulating the kind of structured output needed for HOT-compatible OpenStreetMap tags.

This project was built to get hands-on experience with FastAPI and REST API development before working on a larger geo-image processing pipeline through [Code for Good Berkeley](https://codeforgoodoberkeley.org) in partnership with [Humanitarian OpenStreetMap Team (HOT)](https://www.hotosm.org).

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **FastAPI** | REST API framework |
| **Pillow (PIL)** | Image processing |
| **Uvicorn** | ASGI server |
| **Random** | Mock surface type generation |

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/osm-image-api.git
cd osm-image-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn pillow python-multipart
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

### `GET /status`
Returns a health check confirming the API is running.

```json
{ "status": "OSM Image API is running" }
```

### `POST /analyze-image/`
Upload a street-level image and receive analysis results.

**Request:** `multipart/form-data` with an image file field.

**Response:**
```json
{
  "average_brightness": 142.7,
  "time_of_day": "day",
  "surface_type": "paved",
  "width": 1920,
  "height": 1080,
  "format": "JPEG"
}
```

---

## Purpose

This is a learning project — not production code. It was built to explore FastAPI patterns (routing, file uploads, query parameters, JSON responses) and Python image processing with Pillow before contributing to a real humanitarian mapping system that processes geo-located street imagery for disaster response.

---
