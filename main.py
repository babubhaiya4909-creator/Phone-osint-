from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI(title="Device OSINT API")

# Gemini API Key (Render environment variable)
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


class DeviceRequest(BaseModel):
    device_name: str


@app.get("/")
def home():
    return {"message": "Device OSINT API running"}


@app.post("/device-osint")
def device_osint(data: DeviceRequest):

    prompt = f"""
Bro give me a metadata json osint deep analysis report of device name {data.device_name}
only in json form accepted.
"""

    response = model.generate_content(prompt)

    return {
        "device": data.device_name,
        "osint_report": response.text
    }
