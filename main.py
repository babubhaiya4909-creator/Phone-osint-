from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI(title="Phone OSINT API")

# 🔑 Gemini API Key
API_KEY = "AIzaSyDkiv9RgjPoN4GWiBBg4H2lwcIwJdLZfNM"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


@app.get("/")
def home():
    return {
        "status": "running",
        "usage": "https://phone-osint.onrender.com/{device_name}"
    }


@app.get("/{device_name}")
def device_osint(device_name: str):

    prompt = f"""
Give me a metadata JSON OSINT deep analysis report of device name {device_name}.
Return STRICT JSON only.
No explanation.
"""

    response = model.generate_content(prompt)

    return {
        "query": device_name,
        "report": response.text
    }
