# Voice Reminder - Google Calendar Integration

A web app that listens to voice commands and creates calendar reminders using Claude AI for natural language parsing.

## Setup

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

Run the backend:
```bash
uvicorn main:8000 --reload
```

### 2. Google Calendar OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Calendar API
4. Create OAuth 2.0 credentials (Web Application)
5. Add authorized redirect URIs: `http://localhost:3000`
6. Copy the Client ID

### 3. Frontend Setup

1. Open `index.html` in a browser or serve it locally:
   ```bash
   python -m http.server 3000
   ```

2. Edit `index.html` line 141 and replace `YOUR_GOOGLE_CLIENT_ID_HERE` with your actual Client ID

## How It Works

1. **Voice Input**: Click the microphone button and speak your reminder
2. **Parse**: Claude AI parses the natural language into structured data (title, date, time)
3. **Review**: Edit the parsed reminder if needed
4. **Create**: Click "Create Reminder" to add it to your Google Calendar

## Example Commands

- "Remind me to call mom tomorrow at 3pm"
- "Schedule a meeting with the team next Friday at 10 in the morning"
- "Set a reminder for the dentist appointment on March 15th at 2pm"

## Tech Stack

- **Frontend**: HTML5, Bootstrap, Web Speech API, Google Calendar API
- **Backend**: FastAPI, Claude AI, Python
