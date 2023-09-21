from fastapi import FastAPI
import re
import json
from pydantic import BaseModel

app = FastAPI()

class URLInput(BaseModel):
    url: str

# Load patterns from JSON file
with open("patterns.json", "r") as f:
    patterns = json.load(f)

def identify_youtube_url(url: str):
    for pattern in patterns:
        match = re.search(pattern["regex"], url)
        if match:
            video_id = match.group("video_id")
            return {
                "type": pattern["type"],
                "description": pattern["description"],
                "url": url,
                "meta": {"video_id": video_id}
            }
    
    return {"error": "Not a YouTube URL"}

@app.post("/identify/")
async def identify_url(url_input: URLInput):
    return identify_youtube_url(url_input.url)

@app.get("/")
async def root():
    return {"message": "Welcome to the YouTube URL Identifier! Please use the /identify endpoint to identify a YouTube URL. See the documentation for more details."}
