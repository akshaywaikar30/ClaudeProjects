from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic
import os
from datetime import datetime
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VoiceInput(BaseModel):
    transcript: str

class ParsedReminder(BaseModel):
    title: str
    date: str
    time: str
    description: Optional[str] = None

@app.post("/parse-reminder", response_model=ParsedReminder)
async def parse_reminder(voice_input: VoiceInput):
    """Parse voice transcript into structured reminder data using Claude"""
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    prompt = f"""Parse this voice command into a calendar reminder. Extract:
- title: Brief reminder title
- date: ISO format (YYYY-MM-DD), use today if not specified
- time: HH:MM format (24-hour), use 09:00 if not specified
- description: Optional additional details

Voice command: "{voice_input.transcript}"

Respond in JSON format:
{{
  "title": "...",
  "date": "YYYY-MM-DD",
  "time": "HH:MM",
  "description": "..."
}}

Today's date is {datetime.now().strftime('%Y-%m-%d')}"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    import json
    response_text = message.content[0].text
    json_str = response_text[response_text.find('{'):response_text.rfind('}')+1]
    parsed = json.loads(json_str)
    
    return ParsedReminder(**parsed)

@app.get("/health")
async def health():
    return {"status": "ok"}
