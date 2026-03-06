from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI(title="Device OSINT Analyzer API")

# 🔑 Gemini API Key (direct code me)
API_KEY = "AIzaSyDkiv9RgjPoN4GWiBBg4H2lwcIwJdLZfNM"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


class DeviceRequest(BaseModel):
    device_name: str


@app.get("/")
def home():
    return {
        "status": "running",
        "api": "Device OSINT Analyzer",
        "endpoint": "/device-osint"
    }


@app.post("/device-osint")
def device_osint(request: DeviceRequest):

    device = request.device_name

    prompt = f"""
Bro give me a metadata json osint deep analysis report of device name {device}
only in json form accepted.
"""

    response = model.generate_content(prompt)

    return {
        "device": device,
        "report": response.text
    }
