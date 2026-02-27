from fastapi import FastAPI, UploadFile, File, Query
from PIL import Image
import random
import io



app = FastAPI()

@app.get("/status")
async def status():
    return {"message": "OSM Image API is live lol"}

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...), threshold: int = Query(120)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    gray_image = image.convert("L")
    pixels = list(gray_image.getdata())
    avg_brightness = sum(pixels) / len(pixels)
    if avg_brightness > threshold:
        time_guess = "day"
    else:
        time_guess = "night"

    surface = random.choice(["paved", "unpaved"])


    width, height = image.size
    return {
    "brightness_score": round(avg_brightness, 2),
    "likely_time": time_guess,
    "mock_surface_type": surface,
    "image_dimensions": {"width": width, "height": height},
    "format": image.format
}

    



