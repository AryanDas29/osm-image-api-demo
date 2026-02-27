# OSM Image API Mini-Project

This is a **mini-project** built as part of my preparation for my work with **Humanitarian OpenStreetMap (HOT)** through **Code for Good Berkeley**. The goal of this project was to get familiar with the **FastAPI** tech stack before starting the main HOT project.

---

## Project Description

The **OSM Image API** is a simple API that analyzes uploaded street-level images and returns:

- **Average brightness** of the image
- **Likely time of day** (day/night) based on brightness
- **Mock surface type** (paved/unpaved)
- **Image dimensions** (width, height)
- **Image format** (JPEG, PNG, etc.)

This API uses a combination of **Python**, **FastAPI**, and **Pillow (PIL)** for image processing.

---

## Tech Stack

- **Python** – core programming language
- **FastAPI** – web framework for building the API
- **Pillow (PIL)** – image processing
- **Uvicorn** – ASGI server to run FastAPI
- **Random module** – for mock surface type generation

---

## How to Run

1. # Clone this repository
   git clone https://github.com/AryanDas29/osm-image-api-demo.git
   cd osm-image-api-demo

2. # Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   # venv\Scripts\activate       # Windows

3. # Install dependencies
   pip install fastapi uvicorn pillow python-multipart

4. # Start the FastAPI server
   python -m uvicorn main:app --reload

5. # Open the API docs in your browser
   # http://127.0.0.1:8000/docs

6. # Test the /analyze-image/ endpoint by uploading an image and seeing the JSON response
   # with brightness, likely time, mock surface type, and image metadata